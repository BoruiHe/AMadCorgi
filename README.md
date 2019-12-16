# CIS667-project
1.What is this project?
  As you may guess, this is a variant of Othello (Reversi).
  
2.How to run this code in order (playing without ML -> learning -> playing with ML) and what will you get?
  Downloading otherllo.py and Othello_nointeraction_Main.py to same directory. Run Othello_nointeraction_Main.py and enter proper value as parameters for problem instance size. You will get 4 .npy files that records the score and win rate. The number of times each AI won and cumulative score will be printed on screen.
  
3.What are those files used for?
  They are used for plotting. We provide all the needed code for plotting in two files called plot.py and S_L_nparray.py. Code in S_L_nparray.py could convert .npy file to .npz file. plot.py only takes .npz file as inputs. All the plots in our report comes from plot.py.

4.How could I change other configuration?
  We list all the ocnfiguration parameter here in case you are interested:
  Rate in LRG function or Learning_curve function in othello.py, it refers to learning rate.
  I in untrained_othello or trained_othello function in Othellp_
