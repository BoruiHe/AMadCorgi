import numpy as np
import copy as cp
import random as rd
import matplotlib.pyplot as plt

def plot_performance(a):
    print("a.shape: ", a["untrained"].shape[0])
    x_list_untrain = []
    y_list = []
    for i in range(a["untrained"].shape[0]):
        x_list_untrain.append(a["untrained"][i][0])
        y_list.append(i+1)
    # plt.suptitle('Our AI with Coach AI')
    plt.plot(y_list, x_list_untrain, color='red', label='without MLE')    # YMM
    plt.ylabel('efficiency')
    plt.xlabel('iteration')
    # plt.savefig('./BS4_S6_untrainedAI.png')
    # print(a["untrained"])
    # plt.show()

    print("-------------------------------")
    x_list_train = []
    # y_list_train = []
    for i in range(a["untrained"].shape[0]):
        x_list_train.append(a["trained"][i][0])

    plt.plot(y_list, x_list_train, color='blue', label="AI with MLE")    # YMM
    plt.legend()
    plt.savefig('./YMM_LR0.0005_BS6_S8_(un)trainedAI.png')
    print(a["trained"])
    plt.show()

    print("-------------------------------")
    name_list = ['without MLE', 'AI with MLE']
    AI_win_list = []
    untrain_AI_win = 0.0
    train_AI_win = 0.0

    for i in range(a["untrained"].shape[0]):
        if a["untrained"][i][1] == 1:
            untrain_AI_win = untrain_AI_win + 1
    print("untrain_AI_win: ", untrain_AI_win)
    AI_win_list.append((untrain_AI_win/(a["untrained"].shape[0])))

    for i in range(a["trained"].shape[0]):
        if a["trained"][i][1] == 1:
            train_AI_win = train_AI_win + 1
    AI_win_list.append((train_AI_win/(a["trained"].shape[0])))
    print("train_AI_win: ", train_AI_win)
    plt.bar(range(len(AI_win_list)), AI_win_list, color='rgb', tick_label=name_list)
    plt.suptitle('Win_rate')
    plt.ylabel('win_rate')
    plt.savefig('./YMM_LR0.0005_BS6_S8_win_rate.png')
    plt.show()

    x_list_iteration1 = []
    untrained_babyAI_score = []
    untrained_coachAI_score = []

    trained_babyAI_score = []
    trained_coachAI_score = []

    for i in range(a["untrained"].shape[0]):
        untrained_babyAI_score.append(a["untrained"][i][3])
        untrained_coachAI_score.append(a["untrained"][i][4])
        x_list_iteration1.append(i+1)

    plt.plot(x_list_iteration1, untrained_babyAI_score, color='blue', mfc='w', label='babyAI without MLE')    # YMM
    plt.plot(x_list_iteration1, untrained_coachAI_score, color='red', mfc='w', label='coachAI')    # YMM
    plt.ylabel('score')
    plt.xlabel('iteration')
    plt.legend()
    plt.savefig('./YMM_LR0.0005_BS6_S8_untrained_score.png')
    plt.show()
    x_list_iteration2 = []
    for i in range(a["trained"].shape[0]):
        trained_babyAI_score.append(a["trained"][i][3])
        trained_coachAI_score.append(a["trained"][i][4])
        x_list_iteration2.append(i+1)

    plt.plot(x_list_iteration2, trained_babyAI_score, color='blue', mfc='w', label='babyAI with MLE')    # YMM
    plt.plot(x_list_iteration2, trained_coachAI_score, color='red', mfc='w', label='coachAI')    # YMM
    plt.ylabel('score')
    plt.xlabel('iteration')
    plt.legend()
    plt.savefig('./YMM_LR0.0005_BS6_S8_trained_score.png')
    plt.show()

def plot_lr_curve(a):
    x_list_a = []
    y_list_a = []
    y_list_atrue = []
    print ("a.shape: ", len(a["a"]))
    for i in range(len(a["a"])):
        y_list_a.append(a["a"][i])
        x_list_a.append(i+1)
        y_list_atrue.append(0.7)
    plt.suptitle('learning curve of a')
    plt.plot(x_list_a, y_list_a, color='red', label='a_learning')    # YMM
    plt.plot(x_list_a, y_list_atrue, color='blue', label='a_true')    # YMM
    plt.ylabel('value of a')
    plt.xlabel('iteration')
    plt.legend()
    plt.savefig('./BS8_lc_learning_a_7.png')
    plt.show()

    x_list_b = []
    y_list_b = []
    y_list_btrue = []
    print ("a.shape: ", len(a["b"]))
    for i in range(len(a["b"])):
        y_list_b.append(a["b"][i])
        x_list_b.append(i+1)
        y_list_btrue.append(0.5)
    # plt.suptitle('Our AI with Coach AI')
    plt.suptitle('learning curve of b')
    plt.plot(x_list_b, y_list_b, color='red', label='b_learning')    # YMM
    plt.plot(x_list_b, y_list_btrue, color='blue', label='b_true')    # YMM
    plt.ylabel('value of b')
    plt.xlabel('iteration')
    plt.legend()
    plt.savefig('./BS8_lc_learning_b_5.png')
    plt.show()


if __name__=="__main__":
    perfomance = np.load("YMM_LR0.0005_BS6_S8_aNb.7N.5.npz", allow_pickle= True)
    plot_performance(perfomance)
    learning_curve = np.load("BS8_lc.npz", allow_pickle= True)
    plot_lr_curve(learning_curve)
