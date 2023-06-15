import txt2octl as t2o
import octl2txt as o2t

from util import read_cmd

if __name__=='__main__':
  print(t2o.translate(o2t.translate(read_cmd())))
