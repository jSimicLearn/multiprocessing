import os

def task():
  print("Executing our Task on Process {}".format(os.getpid()))

def main():
  task()
  task()

if __name__ == '__main__':
  main()