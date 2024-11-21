import math
from collections import Counter

def calculate_chunk_entropy(chunk):
    """
    バイトチャンクのエントロピーを計算します。
    
    Args:
        chunk (bytes): バイトデータ
        
    Returns:
        float: エントロピー値
    """
    if not chunk:
        return 0.0
    
    counts = Counter(chunk)
    total = len(chunk)
    entropy = 0
    
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
        
    return entropy

def calculate_file_entropy(file_path):
    """
    ファイル全体の平均エントロピーを計算します。
    
    Args:
        file_path (str): ファイルパス
        
    Returns:
        tuple: (成功フラグ, エントロピー値)
    """
    try:
        chunk_size = 1024
        entropies = []
        
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                entropy = calculate_chunk_entropy(chunk)
                entropies.append(entropy)
        
        if not entropies:
            return False, 0
            
        avg_entropy = sum(entropies) / len(entropies)
        
        return True, avg_entropy
        
    except Exception as e:
        return False, 0