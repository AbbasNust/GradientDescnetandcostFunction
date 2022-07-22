# GradientDescnetandcostFunction
Gradient Descnet and cost Function with Pycharm implementation
Gradient descent is an efficient optimization algorithm that attempts to find a local or global minimum of the cost function
A local minimum is a point where our function is lower than all neighboring points. It is not possible to decrease the value of the cost function by making infinitesimal steps.

A global minimum is a point that obtains the absolute lowest value of our function, but global minima are difficult to compute in practice.
Cost Function vs Gradient descent
Well, a cost function is something we want to minimize. For example, our cost function might be the sum of squared errors over the training set. Gradient descent is a method for finding the minimum of a function of multiple variables.

So we can use gradient descent as a tool to minimize our cost function.

Suppose we have a function with n variables, then the gradient is the length-n vector that defines the direction in which the cost is increasing most rapidly. So in gradient descent, we follow the negative of the gradient to the point where the cost is a minimum. In machine learning, the cost function is a function to which we are applying the gradient descent algorithm.

I assume that the readers are already familiar with calculus but will provide a brief overview of how calculus concepts relate to optimization here. So don’t worry friends, just stay with me… it’s kind of intuitive!

Machine learning uses derivatives in optimization problems. Derivatives are used to decide whether to increase or decrease the weights to increase or decrease an objective function. If we can compute the derivative of a function, we know in which direction to proceed to minimize it.
![image](https://user-images.githubusercontent.com/106056503/180407745-e7c471b8-70ad-4e11-95e7-978cb8c10a09.png)
