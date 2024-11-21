import os
import time
from src.file_processor import read_paths_file, process_paths
from src.utils import time_limit, TimeoutException

def main():
    """
    メイン実行関数。引数の検証とプログラムの実行フローを制御します。
    """
    if os.geteuid() != 0:
        print("root権限で実行してください")
        exit(1)

    if len(os.sys.argv) != 2:
        print("使用方法: python3 script.py <paths_file>")
        exit(1)

    paths_file = os.sys.argv[1]
    if not os.path.exists(paths_file):
        print(f"ファイルが見つかりません: {paths_file}")
        exit(1)

    start_time = time.time()
    valid_paths, extension_filtered, empty_filtered = read_paths_file(paths_file)
    
    if not valid_paths:
        print("有効なパスがありません")
        exit(1)
    
    try:
        with time_limit(600):
            total_files = process_paths(valid_paths)
    except TimeoutException:
        print("\n全体処理タイムアウト")
    except KeyboardInterrupt:
        print("\n中断されました")

if __name__ == "__main__":
    main()