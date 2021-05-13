"""
In perceptron.py, you will implement the perceptron algorithm for
binary classification.  You will implement both the vanilla perceptron
updates as well as the averaged perceptron updates.
"""

import numpy as np

from binary import *
import util
from runClassifier import shufflePoints

class Perceptron(BinaryClassifier):
    """
    This class defines the perceptron implementation of a binary
    classifier.  See binary.py for details on the abstract class that
    this implements.
    """

    def __init__(self, opts):
        """
        Initialize our internal state.  You probably need to (at
        least) keep track of a weight vector and a bias.  We'll just
        call the 'reset' function to do this for us.
        We will also want to compute simple statistics about how the
        training of the perceptron is going.  In particular, you
        should keep track of how many updates have been made total.
        """

        BinaryClassifier.__init__(self, opts)
        self.opts = opts
        self.reset()

    def reset(self):
        """
        Reset the internal state of the classifier.
        """

        self.weights = 0    # our weight vector
        self.bias    = 0    # our bias
        self.numUpd  = 0    # number of updates made

    def online(self):
        """
        Our perceptron is online
        """
        return True

    def __repr__(self):
        """
        Return a string representation of the tree
        """
        return    "w=" + repr(self.weights)   +  ", b=" + repr(self.bias)

    def predict(self, X):
        """
        X is a vector that we're supposed to make a prediction about.
        Our return value should be the margin at this point.
        Semantically, a return value <0 means class -1 and a return
        value >=0 means class +1
        """

        if self.numUpd == 0:
            return 0          # failure
        else:
            return np.dot(self.weights, X) + self.bias   # this is done for you!

    def nextExample(self, X, Y):
        """
        X is a vector training example and Y is its associated class.
        We're guaranteed that Y is either +1 or -1.  We should update
        our weight vector and bias according to the perceptron rule.
        """

        # check to see if we've made an error
        if Y * self.predict(X) <= 0:   ### SOLUTION-AFTER-IF
            self.numUpd  = self.numUpd  + 1

            # perform an update
            self.weights = self.weights + Y * X        ### TODO: YOUR CODE HERE

            self.bias    = self.bias + Y               ### TODO: YOUR CODE HERE

    def nextIteration(self):
        """
        Indicates to us that we've made a complete pass through the
        training data.  This function doesn't need to do anything for
        the perceptron, but might be necessary for other classifiers.
        """
        return   # don't need to do anything here

    def getRepresentation(self):
        """
        Return a tuple of the form (number-of-updates, weights, bias)
        """

        return (self.numUpd, self.weights, self.bias)

    def train(self, X, Y):
        """
        (BATCH ONLY)

        X is a matrix of data points, Y is a vector of +1/-1 classes.
        """
        if self.online():
            for epoch in range(self.opts['numEpoch']):
                # loop over every data point
                for n in range(X.shape[0]):
                    # supply the example to the online learner
                    self.nextExample(X[n], Y[n])

                # tell the online learner that we're
                # done with this iteration
                self.nextIteration()
        else:
            util.raiseNotDefined()


class PermutedPerceptron(Perceptron):

    def train(self, X, Y):
        """
        (BATCH ONLY)

        X is a matrix of data points, Y is a vector of +1/-1 classes.
        """
        if self.online():
            for epoch in range(self.opts['numEpoch']):
                # loop over every data point

                ### TODO: YOUR CODE HERE
                # modify the code here so that the order of the data
                #   will be different each epoch
                # [N,D] = X.shape
                # order = list(range(N))
                # util.permute(order)
                # retX = X[order,:]
                # retY = Y[order]
                X, Y = shufflePoints(X, Y)

                for n in range(X.shape[0]):
                    # supply the example to the online learner
                    self.nextExample(X[n], Y[n])

                # tell the online learner that we're
                # done with this iteration
                self.nextIteration()
        else:
            util.raiseNotDefined()


class AveragedPerceptron(Perceptron):

    def reset(self):
        """
        Reset the internal state of the classifier.
        """

        self.numUpd  = 0    # number of updates made
        self.weights = 0    # our weight vector
        self.bias    = 0    # our bias

        ### TODO: YOUR CODE HERE
        self.u       = 0    # util.raiseNotDefined()    # cached weights
        self.B       = 0    # util.raiseNotDefined()    # chached bias
        self.c       = 1    # util.raiseNotDefined()    # counter

    def nextExample(self, X, Y):
        """
        X is a vector training example and Y is its associated class.
        We're guaranteed that Y is either +1 or -1.  We should update
        our weight vector and bias according to the perceptron rule.
        """

        # check to see if we've made an error
        if Y * self.predict(X) <= 0:   ### SOLUTION-AFTER-IF
            self.numUpd = self.numUpd + 1

            ### TODO: YOUR CODE HERE
            # perform an update
            self.weights = self.weights + Y * X   # util.raiseNotDefined()    # update weights
            self.bias    = self.bias + Y                      # util.raiseNotDefined()    # update bias
            self.u       = self.u + Y * self.c * X            # util.raiseNotDefined() update chached wieghts
            self.B       = self.B + Y * self.c    # util.raiseNotDefined() # updated cached bias

        ### TODO: YOUR CODE HERE
        self.c = self.c + 1                                   # util.raiseNotDefined() # increment counter

    def train(self, X, Y):
        """
        (BATCH ONLY)

        X is a matrix of data points, Y is a vector of +1/-1 classes.
        """
        if self.online():
            for epoch in range(self.opts['numEpoch']):
                # loop over every data point
                for n in range(X.shape[0]):
                    # supply the example to the online learner
                    self.nextExample(X[n], Y[n])

                # tell the online learner that we're
                # done with this iteration
                self.nextIteration()

            ### TODO: YOUR CODE HERE
            self.weights = self.weights - (1/self.c) * self.u  # util.raiseNotDefined()return averaged weights
            self.bias    = self.bias - (1/self.c) * self.B     # util.raiseNotDefined() return averaged bias
        else:
            util.raiseNotDefined()
