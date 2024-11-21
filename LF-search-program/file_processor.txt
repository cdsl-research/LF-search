import os
from src.utils import is_non_log_extension, time_limit, TimeoutException
from src.entropy import calculate_file_entropy

def read_paths_file(file_path):
    """
    入力ファイルを読み込み、有効なパスのリストを返します。
    
    Args:
        file_path (str): 入力ファイルのパス
        
    Returns:
        tuple: (有効なパスのリスト, 拡張子フィルタ数, 空ファイルフィルタ数)
    """
    valid_paths = []
    extension_filtered = 0
    empty_filtered = 0
    
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if line.strip():
                    try:
                        path, is_log = line.strip().rsplit(',', 1)
                        is_log = int(is_log)
                        if os.path.exists(path):
                            if os.path.islink(path) or os.path.getsize(path) == 0:
                                empty_filtered += 1
                                continue
                            if is_non_log_extension(path):
                                extension_filtered += 1
                                continue
                            valid_paths.append((path, is_log))
                    except ValueError:
                        print(f"無効な行形式: {line.strip()}")
                        continue
    except Exception as e:
        print(f"ファイル読み込みエラー: {str(e)}")
        exit(1)
    
    return valid_paths, extension_filtered, empty_filtered

def process_paths(paths):
    """
    パスのリストを処理し、ログファイルを検出します。
    
    Args:
        paths (list): (パス, ログフラグ)のタプルのリスト
        
    Returns:
        int: 処理したファイル数
    """
    file_count = 0
    results = []

    for path, is_log in paths:
        try:
            with time_limit(5):
                success, entropy_rate = calculate_file_entropy(path)
                if success and entropy_rate < 2:
                    results.append(path)
                file_count += 1
        except TimeoutException:
            continue

    print("\n検出したログファイル：")
    for path in results:
        print(path)
    
    return file_count