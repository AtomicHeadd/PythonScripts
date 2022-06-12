import math, os, time

class MassiveLogger:
    def __init__(self, whole_count, log_interval=50000):
        """初期化。最初に100%時の数を計算しておく
        Parameters
        ----------
        whole_count : int
            全体の数
        log_interval : int, optional
            ログを行う数の感覚、10以下など小さすぎる場合パフォーマンスに影響が出る, by default 50000
        """
        self.whole_count = whole_count
        self.interval = log_interval
        self.last_spent_time = 0
        self.last_estimated_time = 0
    
    def start_logging(self):
        """ログ開始時に呼ぶ
        """
        self.start_time = time.perf_counter()

    def log(self, count , whole_count=-1, clear_console=True):
        """ログを表示したいループ内で呼ぶ。インターバルに満たない場合はログの更新をしない
        Parameters
        ----------
        count : int
            現在の数
        whole_count : int, optional 
            全体の数、-1の場合はinit時に与えた値を使用する, by default -1
        """
        if whole_count != -1:self.whole_count = whole_count           
        if count % self.interval != 0: return            
        if clear_console: os.system("clear")           
        spent_time = time.perf_counter() - self.start_time
        estimated_time = int((spent_time / float(count) * float(self.whole_count - count)))
        print_str = str(count) + "/" + str(self.whole_count) + "\n"
        print_str += "実行時間: {:02d}:{:02d}:{:02d}({:=+})\n".format(math.floor(spent_time / 3600), math.floor(spent_time % 3600 / 60), int(spent_time % 60), int(spent_time - self.last_spent_time))
        print_str += "完了まで: {:02d}:{:02d}:{:02d}({:=+})".format(math.floor(estimated_time / 3600), math.floor(estimated_time % 3600 / 60), int(estimated_time % 60), int(-1 * (self.last_estimated_time - estimated_time))) 
        print(print_str)
        self.last_spent_time = spent_time
        self.last_estimated_time = estimated_time  
