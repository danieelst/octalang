import txt2octl as t2o
import octl2txt as o2t

from util import read_cmd

if __name__=='__main__':
  print(o2t.translate(t2o.translate(read_cmd())))
