1. What does a neuron compute?

    - [ ] A neuron computes an activation function followed by a linear function (z = Wx + b)

    - [x] A neuron computes a linear function (z = Wx + b) followed by an activation function

    - [ ] A neuron computes a function g that scales the input x linearly (Wx + b)

    - [ ] A neuron computes the mean of all features before applying the output to an activation function

2. Which of these is the "Logistic Loss"?

    - Check [here](https://en.wikipedia.org/wiki/Cross_entropy#Cross-entropy_error_function_and_logistic_regression).
    
    Note: We are using a cross-entropy loss function.
    
3. Suppose img is a (32,32,3) array, representing a 32x32 image with 3 color channels red, green and blue. How do you reshape this into a column vector?

    - [x] `x = img.reshape((32 * 32 * 3, 1))` // row, columns in the new array
    - [x] `x = img.reshape((-1, 1))` // auto calculated row count, columns

4. Consider the two following random arrays "a" and "b":

    ```
    a = np.random.randn(2, 3) # a.shape = (2, 3)
    b = np.random.randn(2, 1) # b.shape = (2, 1)
    c = a + b
    ```
    
    What will be the shape of "c"?
    2, 3

5. Consider the two following random arrays "a" and "b":

    ```
    a = np.random.randn(4, 3) # a.shape = (4, 3)
    b = np.random.randn(3, 2) # b.shape = (3, 2)
    c = a * b
    ```
    
    What will be the shape of "c"?
    error, because a * b is element wise multiplication and requires a and b either has at least one dimention the same, or one of them to be a 1,  or a unit array

6. Suppose you have n_x input features per example. Recall that X=[x^(1), x^(2)...x^(m)]. What is the dimension of X? n_x, m

7. Recall that `np.dot(a,b)` performs a matrix multiplication on a and b, whereas `a*b` performs an element-wise multiplication.

    Consider the two following random arrays "a" and "b":

    ```
    a = np.random.randn(12288, 150) # a.shape = (12288, 150)
    b = np.random.randn(150, 45) # b.shape = (150, 45)
    c = np.dot(a, b)
    ```
    
    What is the shape of c?
    12288, 45

8. Consider the following code snippet:

    ```
    # a.shape = (3,4)
    # b.shape = (4,1)
    for i in range(3):
      for j in range(4):
        c[i][j] = a[i][j] + b[j]
    ```
    
    How do you vectorize this?
    a + b.T

9. Consider the following code:

    ```
    a = np.random.randn(3, 3)
    b = np.random.randn(3, 1)
    c = a * b
    ```
    
    What will be c? element wise multiplication of a by column with elements in b

10. Consider the following computation graph. What is J in simplified form, given J = a * b + a * c - (b + c)? Answer: (a-1) * (b+c)

Note: This quiz is taken from this [link](https://github.com/Kulbear/deep-learning-coursera/blob/master/Neural%20Networks%20and%20Deep%20Learning/Week%202%20Quiz%20-%20Neural%20Network%20Basics.md)
