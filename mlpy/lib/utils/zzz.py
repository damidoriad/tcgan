class AvgrageMeter(object):
    """copy from https://github.com/quark0/darts/blob/master/cnn/utils.py"""

    def __init__(self):
        self.reset()

    def reset(self):
        self.avg = 0
        self.sum = 0
        self.cnt = 0

    def update(self, val, n=1):
        self.sum += val * n
        self.cnt += n
        self.avg = self.sum / self.cnt