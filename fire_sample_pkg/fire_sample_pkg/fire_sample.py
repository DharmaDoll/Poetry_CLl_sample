#!/usr/bin/env python

# Following preparation is required
# 'poetry add fire' or `pip install fire`
import fire

class SubCmd1(object):
    '''サブ１だよ'''
    def __init__(self, _opt1, _opt2):
        self._opt1 = _opt1
        self._opt2 = _opt2

    def run(self):
        return f'Sub cmd1! Nom nom nom... {self._opt1}, {self._opt2}'

class SubCmd2(object):
    '''サブ２だよ'''
    def __init__(self, _opt1):
        self._opt1 = _opt1

    def run(self, volume=1):
        print(f'opt1: {self._opt1}')
        print(' '.join(['Burp! sub cmd2 '] * volume))
        # return ' '.join(['Burp!'] * volume)

    def status(self):
        return 'Satiated.'

class Pipeline(object):
    '''パイプラインだよ。コマンドサンプルはhelpコマンドで確認！'''
    #共通のパラメタをここでセット。必須はデフォルト引数なしにしちゃうと(fireの)help画面がいい感じにならない
    def __init__(self, opt1='', opt2=''):
        self.sub1 = SubCmd1(opt1, opt2)
        self.sub2 = SubCmd2(opt1)
        self.opt1 = opt1
        self.opt2 = opt2

    def help(self):
        print(f"""
Usage:
    {__file__} -opt1 <value> -opt2 <value>
    {__file__} sub2 -opt1 <valur> -volume <value>
""")

    # 各メソッドで戻りを受け取って処理とかしないとcli上では何も表示されないので注意
    def run(self):
        self.sub1.run()
        self.sub2.run()

    def base_function(self):
        print(self.__dir__())

def main():
    fire.Fire(Pipeline)

if __name__ == '__main__':
    main()


# class Building(object):

#   def __init__(self, name, stories=1):
#     self.name = name
#     self.stories = stories
#     print(name, stories)

#   def climb_stairs(self, stairs_per_story=10):
#     for story in range(self.stories):
#       for stair in range(1, stairs_per_story):
#         yield stair
#       yield 'Phew!'
#     yield 'Done!'

# if __name__ == '__main__':
#   fire.Fire(Building)



# import fire

# def usage():
# 	print('uuusage')

# def single_cmd(p1, f='./',o='./', p2=''):
#     f'''
#    usage :{__file__}dayotest
#     vvvq
#     '''
    
#     print(f'p1: {p1}')
#     print(f'f: {f}')
#     print(f'p2: {p2}')

# if __name__ == "__main__":
#     print(f'It is main! {__file__}')
#     fire.Fire(single_cmd)
#     #fire.Fire()
