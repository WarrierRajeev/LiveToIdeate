import numpy as np

def Sigmoid(z):
	G_of_z = float(1.0/float(1.0+np.exp(-1.0*z)))
	return G_of_z

def Hypothesis(X, Theta):
	''' This function gives the h_theta(X) or the hypothesis function.
		Here X should be an numpy array of dimensions (n,m) where all n = 0 elements are equal to 1. 
		Theta is the 1-D parameters vector.
	'''
	z = np.dot(X, np.transpose(Theta))
	return Sigmoid(z)

def CostFunction(X,Y,Theta):
	h_of_x = Hypothesis(X,Theta)
	SumOfErrors = np.dot(Y, h_of_x) + np.dot((1.0-Y),(1.0-h_of_x))
	J = (-1.0/len(Y))*SumOfErrors
	return J

def CostDerivative(X,Y,Theta):
	''' This function gives the derivative of cost function of logistic regression.
		alpha is the learning rate.
	'''
	return (1.0/len(Y))*(np.multiply(Hypothesis(X,Theta) - np.transpose(Y)),X[:,])

def GradientDescent(X,Y,Theta,alpha=0.01,n_i):
	''' This function performs Gradient Descent and updates the parameters and returns 
		the new Theta.
		n_i is the number of iterations
	'''
	Theta_new = np.matrix(np.zeros(theta.shape))
    cost = np.zeros(iters)

	for i in range(n_i):

		Theta_new = Theta - alpha * CostDerivative(X,Y,Theta).sum(axis = 0)
		Theta = Theta_new
		cost[i] = CostFunction(X,Y,Theta)

	return Theta, cost







