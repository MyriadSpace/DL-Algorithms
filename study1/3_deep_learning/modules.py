import tensorflow as tf
    
def single_layer_perceptron(input, output_dim=None):

    input_dim = input.shape[1].value

    weight = tf.Variable(
        tf.truncated_normal([input_dim, output_dim], stddev=0.1),
        name="weight"
    )
    bias = tf.Variable(
        tf.zeros([output_dim]), 
        name="bias"
    )
    output = tf.add(tf.matmul(input, weight), bias)
    return output

def _single_layer_perceptron(input, output_dim=10):

    input_dim = input.shape[1].value
    with tf.name_scope(name="slp"):
        with tf.variable_scope("params", reuse=tf.AUTO_REUSE):
            weight = tf.get_variable(
                "wegiht", 
                shape=[input_dim, output_dim],
                dtype=tf.float32,
                initializer=tf.truncated_normal_initializer(mean=0, stddev=0.1)
            )
            bias = tf.get_variable(
                "bias",
                shape=[output_dim],
                dtype=tf.float32,
                initializer=tf.constant_initializer([0.0]) 
            )
    output = tf.add(tf.matmul(input, weight), bias)
    return output

def dense_layer(input, output_dim=None, name=None):

    input_dim = input.shape[1].value

    with tf.name_scope(name=name):
        with tf.variable_scope(name+"/params", reuse=tf.AUTO_REUSE):
            weight = tf.get_variable(
                "wegiht", 
                shape=[input_dim, output_dim],
                dtype=tf.float32,
                initializer=tf.truncated_normal_initializer(mean=0, stddev=0.1)
            )
            bias = tf.get_variable(
                "bias",
                shape=[output_dim],
                dtype=tf.float32,
                initializer=tf.constant_initializer([0.0]) 
            )
    return tf.add(tf.matmul(input, weight), bias)

def multi_layer_perceptron(input, output_dim=None):

    input_to_hidden1 = dense_layer(
        input, 
        output_dim=128,
        name="hidden1"
    )
    input_to_hidden1 = tf.nn.relu(input_to_hidden1)
    hidden1_to_hidden2 = dense_layer(
        input_to_hidden1, 
        output_dim=64,
        name="hidden2"
    )
    hidden1_to_hidden2 = tf.nn.relu(hidden1_to_hidden2)
    hidden2_to_output = dense_layer(
        hidden1_to_hidden2, 
        output_dim=10,
        name="output"
    )
    return hidden2_to_output


def convolutional_neural_network(input=None, output_dim=None):

    input_dim = input.shape[1].value
    reshape_dim = int(input_dim**0.5)

    image = tf.reshape(input, [-1, reshape_dim, reshape_dim, 1])
    conv1 = conv_layer(image, name="conv1")
    conv1 = tf.nn.tanh(conv1)
    max_pool1 = max_pool_layer(conv1, name="max_pool1")
    conv2 = conv_layer(max_pool1, name="conv2")
    conv2 = tf.nn.tanh(conv2)
    max_pool2 = max_pool_layer(conv2, name="max_pool2")

    max_pool2 = tf.reshape(max_pool2, [-1, max_pool2.shape[1].value])

    fc1 = dense_layer(max_pool2, output_dim=500, name="fc1")
    fc1 = tf.nn.tanh(fc1)
    output = dense_layer(fc1, output_dim=10)
    return output

def conv_layer(input, name=None):
    output = 0
    return output

def max_pool_layer(input, name=None):
    output = 0 
    return output

#test

# with tf.Session() as sess:
#     input = tf.placeholder(tf.float32, [None, 28*28])
#     prediction = single_layer_percentorn(input, input_dim=28, output_dim=10)
