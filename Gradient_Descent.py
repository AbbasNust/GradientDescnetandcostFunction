import numpy as np

def grad_descent(x,y):
     m_cuur= b_curr=0
     iteration= 10
     n= len(x)
     lr= 0.001

     for i in range (iteration):
         y_predicted = m_cuur*x +b_curr
         cost= (1/n)*sum([val**2 for val in (y- y_predicted  )])
         m_derivative= -(2/n)*sum(x*(y-y_predicted))
         b_derivative= -(2/n)*sum(y-y_predicted)
         m_cuur= m_cuur - lr*m_derivative
         b_curr= b_curr- lr*b_derivative
         print("m {}, b{} , iteration{}". format(m_cuur,b_curr,cost, i))

x= np.array([1, 2,3 ,4 ,5])
y=np.array([5,7,9,11,13])
grad_descent(x, y)
