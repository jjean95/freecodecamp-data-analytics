import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.") #to eliminate any list with less than 9 numbers
      
  ls = np.array(list).reshape(3,3) #change list into an array, and reshape it into 3X3
  #calculate mean for axis 0 and axis 1
  cal_mean_ax0 = ls.mean(axis=0).tolist()
  cal_mean_ax1 = ls.mean(axis=1).tolist()
  #calculate variance for axis 0 and axis 1
  cal_var_ax0 = ls.var(axis=0).tolist()
  cal_var_ax1 = ls.var(axis=1).tolist()
  #calculate standard deviation for axis 0 and axis 1
  cal_std_ax0 = ls.std(axis=0).tolist()
  cal_std_ax1 = ls.std(axis=1).tolist()
  #calculate maximum for axis 0 and axis 1
  cal_max_ax0 = ls.max(axis=0).tolist()
  cal_max_ax1 = ls.max(axis=1).tolist()
  #calculate minimum for axis 0 and axis 1
  cal_min_ax0 = ls.min(axis=0).tolist()
  cal_min_ax1 = ls.min(axis=1).tolist()
  #calculate sum for axis 0 and axis 1
  cal_sum_ax0 = ls.sum(axis=0).tolist()
  cal_sum_ax1 = ls.sum(axis=1).tolist()
  
  return {
    'mean' : [cal_mean_ax0,cal_mean_ax1,np.mean(ls)],
    'variance' : [cal_var_ax0,cal_var_ax1,np.var(ls)],
    'standard deviation': [cal_std_ax0,cal_std_ax1,np.std(ls)],
    'max': [cal_max_ax0,cal_max_ax1,np.max(ls)],
    'min': [cal_min_ax0,cal_min_ax1,np.min(ls)],
    'sum': [cal_sum_ax0,cal_sum_ax1,np.sum(ls)]
  }

