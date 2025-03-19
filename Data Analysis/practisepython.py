{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPqp0/iSRUjEXSLs0JAsRfU",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Esheshwari/python-programming/blob/main/Data%20Analysis/practisepython.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9Ajrijh3pqm_",
        "outputId": "9b4a374b-ebc1-4bd2-fd7b-38b48406d2f2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Array from 1 to 10: [ 1  2  3  4  5  6  7  8  9 10]\n",
            "Equally spaced array between 0 and 1: [0.         0.05263158 0.10526316 0.15789474 0.21052632 0.26315789\n",
            " 0.31578947 0.36842105 0.42105263 0.47368421 0.52631579 0.57894737\n",
            " 0.63157895 0.68421053 0.73684211 0.78947368 0.84210526 0.89473684\n",
            " 0.94736842 1.        ]\n",
            "Random integers between 1 and 100: [ 7 46 85 49 58 42 72 93 46 16]\n"
          ]
        }
      ],
      "source": [
        "'''Question 1\n",
        "1D Arrays\n",
        "Create a 1D NumPy array from a list of numbers from 1 to 10.\n",
        "Create a 1D array of 20 equally spaced numbers between 0 and 1.\n",
        "Generate a 1D array of 10 random integers between 1 and 100.'''\n",
        "import numpy as np\n",
        "\n",
        "# 1. Create a 1D NumPy array from a list of numbers from 1 to 10\n",
        "array_1_to_10 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])\n",
        "\n",
        "# 2. Create a 1D array of 20 equally spaced numbers between 0 and 1\n",
        "equally_spaced_array = np.linspace(0, 1, 20)\n",
        "\n",
        "# 3. Generate a 1D array of 10 random integers between 1 and 100\n",
        "random_integers = np.random.randint(1, 101, 10)\n",
        "\n",
        "# Print results\n",
        "print(\"Array from 1 to 10:\", array_1_to_10)\n",
        "print(\"Equally spaced array between 0 and 1:\", equally_spaced_array)\n",
        "print(\"Random integers between 1 and 100:\", random_integers)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'''Question 2\n",
        "2D Arrays\n",
        "Create a 2D array with 3 rows and 4 columns filled with zeros.\n",
        "Generate a 2D array with the shape (5,5) containing random floating-point numbers.\n",
        "Create a 2x2 identity matrix.'''\n",
        "import numpy as np\n",
        "\n",
        "# 1. Create a 2D array with 3 rows and 4 columns filled with zeros\n",
        "zeros_array = np.zeros((3, 4))\n",
        "\n",
        "# 2. Generate a 2D array with the shape (5,5) containing random floating-point numbers\n",
        "random_floats_array = np.random.random((5, 5))\n",
        "\n",
        "# 3. Create a 2x2 identity matrix\n",
        "identity_matrix = np.eye(2)\n",
        "\n",
        "# Print results\n",
        "print(\"2D Array filled with zeros (3x4):\\n\", zeros_array)\n",
        "print(\"Random floating-point numbers array (5x5):\\n\", random_floats_array)\n",
        "print(\"2x2 Identity matrix:\\n\", identity_matrix)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QfHUhF0Tr09P",
        "outputId": "a54b0952-e981-4bbd-a988-9ddbb44c0a6f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2D Array filled with zeros (3x4):\n",
            " [[0. 0. 0. 0.]\n",
            " [0. 0. 0. 0.]\n",
            " [0. 0. 0. 0.]]\n",
            "Random floating-point numbers array (5x5):\n",
            " [[0.96043483 0.87558167 0.68839767 0.22625285 0.15648513]\n",
            " [0.95325762 0.18924903 0.18039338 0.73475072 0.7565032 ]\n",
            " [0.37605665 0.79101636 0.16233635 0.56971523 0.42459451]\n",
            " [0.12949876 0.91112357 0.26607258 0.90259849 0.31639987]\n",
            " [0.28314391 0.57778677 0.89618072 0.80666933 0.6669872 ]]\n",
            "2x2 Identity matrix:\n",
            " [[1. 0.]\n",
            " [0. 1.]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'''Create a 3D array with the shape (3,4,2) filled with zeros.\n",
        "Generate a 3D array with the shape (2,3,3) containing random integers between 1 and 10.\n",
        "Convert a list of 24 sequential numbers into a 3D array with shape (2,3,4).\n",
        "Calculate the mean alongthe row and column.\n",
        "Calculate the mean. '''\n",
        "import numpy as np\n",
        "\n",
        "# 1. Create a 3D array with the shape (3, 4, 2) filled with zeros\n",
        "zeros_3d_array = np.zeros((3, 4, 2))\n",
        "\n",
        "# 2. Generate a 3D array with the shape (2, 3, 3) containing random integers between 1 and 10\n",
        "random_ints_3d_array = np.random.randint(1, 11, (2, 3, 3))\n",
        "\n",
        "# 3. Convert a list of 24 sequential numbers into a 3D array with shape (2, 3, 4)\n",
        "sequential_numbers = np.arange(1, 25)  # List of 24 numbers from 1 to 24\n",
        "sequential_3d_array = sequential_numbers.reshape(2, 3, 4)\n",
        "\n",
        "# 4. Calculate the mean along the row (axis=1) and column (axis=2)\n",
        "mean_along_rows = sequential_3d_array.mean(axis=1)  # Mean along rows\n",
        "mean_along_columns = sequential_3d_array.mean(axis=2)  # Mean along columns\n",
        "mean_of_3d_array = sequential_3d_array.mean()\n",
        "\n",
        "# Print results\n",
        "print(\"3D Array filled with zeros (3x4x2):\\n\", zeros_3d_array)\n",
        "print(\"\\nRandom integers array (2x3x3):\\n\", random_ints_3d_array)\n",
        "print(\"\\n3D Array from sequential numbers (2x3x4):\\n\", sequential_3d_array)\n",
        "print(\"\\nMean along rows (axis=1):\\n\", mean_along_rows)\n",
        "print(\"\\nMean along columns (axis=2):\\n\", mean_along_columns)\n",
        "print(\"\\nMean of the entire 3D array:\\n\", mean_of_3d_array)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KdsqW0r1tyO3",
        "outputId": "1c40e5f2-3c94-4a6e-b42c-3850b3ec47db"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3D Array filled with zeros (3x4x2):\n",
            " [[[0. 0.]\n",
            "  [0. 0.]\n",
            "  [0. 0.]\n",
            "  [0. 0.]]\n",
            "\n",
            " [[0. 0.]\n",
            "  [0. 0.]\n",
            "  [0. 0.]\n",
            "  [0. 0.]]\n",
            "\n",
            " [[0. 0.]\n",
            "  [0. 0.]\n",
            "  [0. 0.]\n",
            "  [0. 0.]]]\n",
            "\n",
            "Random integers array (2x3x3):\n",
            " [[[ 3  7  8]\n",
            "  [ 3  8  4]\n",
            "  [ 4  3  7]]\n",
            "\n",
            " [[ 1  1  4]\n",
            "  [ 5  6  5]\n",
            "  [ 1  8 10]]]\n",
            "\n",
            "3D Array from sequential numbers (2x3x4):\n",
            " [[[ 1  2  3  4]\n",
            "  [ 5  6  7  8]\n",
            "  [ 9 10 11 12]]\n",
            "\n",
            " [[13 14 15 16]\n",
            "  [17 18 19 20]\n",
            "  [21 22 23 24]]]\n",
            "\n",
            "Mean along rows (axis=1):\n",
            " [[ 5.  6.  7.  8.]\n",
            " [17. 18. 19. 20.]]\n",
            "\n",
            "Mean along columns (axis=2):\n",
            " [[ 2.5  6.5 10.5]\n",
            " [14.5 18.5 22.5]]\n",
            "\n",
            "Mean of the entire 3D array:\n",
            " 12.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'''Create a 3D array with the shape (2,3,4) filled with ones.\n",
        "Generate a 4D array with the shape (2,2,2,2) containing all zeros'''\n",
        "import numpy as np\n",
        "\n",
        "# 1. Create a 3D array with the shape (2, 3, 4) filled with ones\n",
        "ones_3d_array = np.ones((2, 3, 4))\n",
        "\n",
        "# 2. Generate a 4D array with the shape (2, 2, 2, 2) containing all zeros\n",
        "zeros_4d_array = np.zeros((2, 2, 2, 2))\n",
        "\n",
        "# Print results\n",
        "print(\"3D Array filled with ones (2x3x4):\\n\", ones_3d_array)\n",
        "print(\"\\n4D Array filled with zeros (2x2x2x2):\\n\", zeros_4d_array)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Sj06AAGHv4qQ",
        "outputId": "20b8d23d-9fb6-427f-e782-0027a5de0ed6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3D Array filled with ones (2x3x4):\n",
            " [[[1. 1. 1. 1.]\n",
            "  [1. 1. 1. 1.]\n",
            "  [1. 1. 1. 1.]]\n",
            "\n",
            " [[1. 1. 1. 1.]\n",
            "  [1. 1. 1. 1.]\n",
            "  [1. 1. 1. 1.]]]\n",
            "\n",
            "4D Array filled with zeros (2x2x2x2):\n",
            " [[[[0. 0.]\n",
            "   [0. 0.]]\n",
            "\n",
            "  [[0. 0.]\n",
            "   [0. 0.]]]\n",
            "\n",
            "\n",
            " [[[0. 0.]\n",
            "   [0. 0.]]\n",
            "\n",
            "  [[0. 0.]\n",
            "   [0. 0.]]]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'''Given a 1D array [3, 7, 2, 9, 5, 8, 1], extract the elements at indices 1, 3, and 5.\n",
        "From a 2D array with shape (4,5), extract the element at row 2, column 3.\n",
        "From a 2D array, extract the entire second row.\n",
        "From a 2D array, extract a subarray containing rows 1 to 3 and columns 2 to 4.'''\n",
        "import numpy as np\n",
        "\n",
        "# 1. Given a 1D array [3, 7, 2, 9, 5, 8, 1], extract the elements at indices 1, 3, and 5\n",
        "array_1d = np.array([3, 7, 2, 9, 5, 8, 1])\n",
        "extracted_elements = array_1d[[1, 3, 5]]\n",
        "\n",
        "# 2. From a 2D array with shape (4,5), extract the element at row 2, column 3\n",
        "array_2d = np.array([[10, 20, 30, 40, 50],\n",
        "                     [60, 70, 80, 90, 100],\n",
        "                     [110, 120, 130, 140, 150],\n",
        "                     [160, 170, 180, 190, 200]])\n",
        "element_at_2_3 = array_2d[2, 3]\n",
        "\n",
        "# 3. From a 2D array, extract the entire second row\n",
        "second_row = array_2d[1, :]\n",
        "\n",
        "# 4. From a 2D array, extract a subarray containing rows 1 to 3 and columns 2 to 4\n",
        "subarray = array_2d[1:4, 2:5]\n",
        "\n",
        "# Print results\n",
        "print(\"Extracted elements from 1D array:\", extracted_elements)\n",
        "print(\"Element at row 2, column 3 in 2D array:\", element_at_2_3)\n",
        "print(\"Second row from 2D array:\", second_row)\n",
        "print(\"Subarray from 2D array (rows 1 to 3, columns 2 to 4):\\n\", subarray)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zd4k2RAOwaKB",
        "outputId": "c45c1458-3f69-46f1-d26b-5ab3762ddd15"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Extracted elements from 1D array: [7 9 8]\n",
            "Element at row 2, column 3 in 2D array: 140\n",
            "Second row from 2D array: [ 60  70  80  90 100]\n",
            "Subarray from 2D array (rows 1 to 3, columns 2 to 4):\n",
            " [[ 80  90 100]\n",
            " [130 140 150]\n",
            " [180 190 200]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'''From a 3D array with shape (3,4,5), extract the element at position (depth 1,row 2,col 3).\n",
        "From a 3D array, extract the entire first \"layer\" (all rows and columns of the first depth index).\n",
        "From a 3D array of shape (4,5,6), extract a subarray containing depths 1 to 3, rows 2 to 4, and columns 3 to 5.'''\n",
        "import numpy as np\n",
        "\n",
        "# Create a 3D array with shape (3, 4, 5)\n",
        "array_3d = np.random.randint(1, 100, (3, 4, 5))\n",
        "\n",
        "# 1. Extract the element at position (depth 1, row 2, col 3)\n",
        "element_at_position = array_3d[1, 2, 3]\n",
        "\n",
        "# 2. Extract the entire first \"layer\" (all rows and columns of the first depth index)\n",
        "first_layer = array_3d[0, :, :]\n",
        "\n",
        "# 3. Extract a subarray from a 3D array of shape (4, 5, 6) containing depths 1 to 3, rows 2 to 4, and columns 3 to 5\n",
        "array_3d_large = np.random.randint(1, 100, (4, 5, 6))\n",
        "subarray = array_3d_large[1:4, 2:5, 3:6]\n",
        "\n",
        "# Print results\n",
        "print(\"Element at position (depth 1, row 2, col 3):\", element_at_position)\n",
        "print(\"\\nEntire first 'layer' (depth 0):\\n\", first_layer)\n",
        "print(\"\\nSubarray from depths 1 to 3, rows 2 to 4, and columns 3 to 5:\\n\", subarray)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c5MQXOTCxsv3",
        "outputId": "1e60d999-a9dc-4152-c26f-1682fb44ce8f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Element at position (depth 1, row 2, col 3): 70\n",
            "\n",
            "Entire first 'layer' (depth 0):\n",
            " [[82 41 19 23 82]\n",
            " [91 48 14 77 19]\n",
            " [61 79 50 22 43]\n",
            " [13 37 95 69 16]]\n",
            "\n",
            "Subarray from depths 1 to 3, rows 2 to 4, and columns 3 to 5:\n",
            " [[[98 41 90]\n",
            "  [53 94 26]\n",
            "  [ 3  1  2]]\n",
            "\n",
            " [[ 5 30 17]\n",
            "  [93 72 83]\n",
            "  [62 66 17]]\n",
            "\n",
            " [[40 30 82]\n",
            "  [63 73 21]\n",
            "  [97  4 36]]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'''Reshape a 1D array of 12 elements into a 3x4 2D array.\n",
        "Reshape a 2D array of shape (3,4) into a 1D array.\n",
        "Transpose a 2D array of shape (2,5).'''\n",
        "import numpy as np\n",
        "\n",
        "# 1. Reshape a 1D array of 12 elements into a 3x4 2D array\n",
        "array_1d = np.arange(1, 13)  # 1D array with 12 elements\n",
        "reshaped_2d = array_1d.reshape(3, 4)\n",
        "\n",
        "# 2. Reshape a 2D array of shape (3,4) into a 1D array\n",
        "array_2d = np.array([[1, 2, 3, 4],\n",
        "                     [5, 6, 7, 8],\n",
        "                     [9, 10, 11, 12]])\n",
        "reshaped_1d = array_2d.reshape(-1)\n",
        "\n",
        "# 3. Transpose a 2D array of shape (2, 5)\n",
        "array_2d_transpose = np.array([[1, 2, 3, 4, 5],\n",
        "                                [6, 7, 8, 9, 10]])\n",
        "transposed_array = array_2d_transpose.T  # or array_2d_transpose.transpose()\n",
        "\n",
        "# Print results\n",
        "print(\"Reshaped 1D array into 3x4 2D array:\\n\", reshaped_2d)\n",
        "print(\"\\nReshaped 2D array into 1D array:\\n\", reshaped_1d)\n",
        "print(\"\\nTransposed 2D array (2,5) into (5,2):\\n\", transposed_array)\n"
      ],
      "metadata": {
        "id": "oyEG2OSuz3oe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "'''Reshape a 3D array of shape (2,3,4) into a 2D array of shape (6,4).\n",
        "Transpose a 3D array, swapping the first and third dimensions.\n",
        "Stack two 2D arrays of shape (3,4) to create a 3D array of shape (2,3,4).'''\n",
        "import numpy as np\n",
        "\n",
        "# 1. Reshape a 3D array of shape (2, 3, 4) into a 2D array of shape (6, 4)\n",
        "arr_3d = np.arange(1, 25).reshape(2, 3, 4)\n",
        "reshaped_2d = arr_3d.reshape(6, 4)\n",
        "\n",
        "# 2. Transpose a 3D array, swapping the first and third dimensions\n",
        "transposed_3d = arr_3d.transpose(2, 1, 0)\n",
        "\n",
        "# 3. Stack two 2D arrays of shape (3, 4) to create a 3D array of shape (2, 3, 4)\n",
        "arr_2d_1 = np.random.randint(1, 10, (3, 4))\n",
        "arr_2d_2 = np.random.randint(1, 10, (3, 4))\n",
        "stacked_3d = np.stack((arr_2d_1, arr_2d_2), axis=0)\n",
        "\n",
        "# Print results\n",
        "print(\"Reshaped 3D to 2D (6x4):\\n\", reshaped_2d)\n",
        "print(\"\\nTransposed 3D array:\\n\", transposed_3d)\n",
        "print(\"\\nStacked 2D arrays into 3D (2,3,4):\\n\", stacked_3d)\n"
      ],
      "metadata": {
        "id": "dCpDhY9-0tez"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "'''Add two 1D arrays of the same length element-wise.\n",
        "Multiply a 2D array by a scalar value.\n",
        "Calculate the square root of each element in an array.'''\n",
        "import numpy as np\n",
        "\n",
        "# 1. Add two 1D arrays of the same length element-wise\n",
        "arr1 = np.array([1, 2, 3, 4, 5])\n",
        "arr2 = np.array([5, 4, 3, 2, 1])\n",
        "added_arrays = arr1 + arr2\n",
        "\n",
        "# 2. Multiply a 2D array by a scalar value\n",
        "arr_2d = np.array([[1, 2, 3], [4, 5, 6]])\n",
        "scalar_value = 3\n",
        "multiplied_array = arr_2d * scalar_value\n",
        "\n",
        "# 3. Calculate the square root of each element in an array\n",
        "arr = np.array([1, 4, 9, 16, 25])\n",
        "sqrt_array = np.sqrt(arr)\n",
        "\n",
        "# Print results\n",
        "print(\"Added 1D arrays element-wise:\", added_arrays)\n",
        "print(\"\\n2D array multiplied by scalar:\", multiplied_array)\n",
        "print(\"\\nSquare root of each element in the array:\", sqrt_array)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nHyyXY7P1nvh",
        "outputId": "c776e77b-7242-4fc3-87d8-80277eabc9bb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Added 1D arrays element-wise: [6 6 6 6 6]\n",
            "\n",
            "2D array multiplied by scalar: [[ 3  6  9]\n",
            " [12 15 18]]\n",
            "\n",
            "Square root of each element in the array: [1. 2. 3. 4. 5.]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'''Perform element-wise addition between two 3D arrays of the same shape.\n",
        "Calculate the mean along the second axis of a 3D array.\n",
        "Apply a function (like np.sin) to each element of a 3D array.'''\n",
        "import numpy as np\n",
        "\n",
        "# 1. Perform element-wise addition between two 3D arrays of the same shape\n",
        "arr1_3d = np.random.randint(1, 10, (2, 3, 4))  # A random 3D array of shape (2, 3, 4)\n",
        "arr2_3d = np.random.randint(1, 10, (2, 3, 4))  # Another random 3D array of the same shape\n",
        "added_3d_arrays = arr1_3d + arr2_3d\n",
        "\n",
        "# 2. Calculate the mean along the second axis (axis=1) of a 3D array\n",
        "mean_second_axis = arr1_3d.mean(axis=1)\n",
        "\n",
        "# 3. Apply a function (like np.sin) to each element of a 3D array\n",
        "sin_of_3d = np.sin(arr1_3d)\n",
        "\n",
        "# Print results\n",
        "print(\"Element-wise addition of two 3D arrays:\\n\", added_3d_arrays)\n",
        "print(\"\\nMean along the second axis (axis=1):\\n\", mean_second_axis)\n",
        "print(\"\\nSin of each element in the 3D array:\\n\", sin_of_3d)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uRkF9T5V3c2D",
        "outputId": "fe1b7552-8d68-4789-a37c-2bfc4f7346b0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Element-wise addition of two 3D arrays:\n",
            " [[[13 11  6 11]\n",
            "  [10 12 12 11]\n",
            "  [14 17  8  4]]\n",
            "\n",
            " [[ 9  5 14  7]\n",
            "  [10 10  9 14]\n",
            "  [10  8  6  4]]]\n",
            "\n",
            "Mean along the second axis (axis=1):\n",
            " [[4.         7.33333333 5.33333333 3.66666667]\n",
            " [7.         3.66666667 6.33333333 4.        ]]\n",
            "\n",
            "Sin of each element in the 3D array:\n",
            " [[[-0.95892427  0.41211849  0.14112001 -0.7568025 ]\n",
            "  [ 0.90929743 -0.95892427  0.6569866  -0.2794155 ]\n",
            "  [-0.95892427  0.98935825 -0.2794155   0.84147098]]\n",
            "\n",
            " [[-0.95892427  0.14112001  0.41211849  0.14112001]\n",
            "  [ 0.6569866   0.14112001 -0.2794155   0.98935825]\n",
            "  [ 0.41211849 -0.95892427 -0.7568025   0.84147098]]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#V.IMP FOR EXAM\n",
        "import numpy as np\n",
        "np.random.seed(100)\n",
        "test=np.random.randint(1,101,(3,4,5))#understand how is it cal mean\n",
        "print(test)\n",
        "print(np.mean(test, axis=0))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7IWGcvzf4VBX",
        "outputId": "cde89dc3-dcec-453c-b8ad-38ec992658c8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[[ 9 25 68 88 80]\n",
            "  [49 11 95 53 99]\n",
            "  [54 67 99 15 35]\n",
            "  [25 16 61 59 17]]\n",
            "\n",
            " [[10 94 87  3 28]\n",
            "  [ 5 32  2 14 84]\n",
            "  [ 5 92 60 68  8]\n",
            "  [50 48 66 62 15]]\n",
            "\n",
            " [[56 72 81  3 95]\n",
            "  [20 99 64 54 28]\n",
            "  [57 31 49 48 40]\n",
            "  [39 45 19 65 57]]]\n",
            "[[25.         63.66666667 78.66666667 31.33333333 67.66666667]\n",
            " [24.66666667 47.33333333 53.66666667 40.33333333 70.33333333]\n",
            " [38.66666667 63.33333333 69.33333333 43.66666667 27.66666667]\n",
            " [38.         36.33333333 48.66666667 62.         29.66666667]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#V.IMP FOR EXAM\n",
        "import numpy as np\n",
        "np.random.seed(100)\n",
        "test=np.random.randint(1,101,(3,4,5))#understand how is it cal mean\n",
        "print(test)\n",
        "print(np.mean(test, axis=2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FLvMHO0Y5HMZ",
        "outputId": "a68f8af6-ad84-4a63-be59-a4d54f9e0c48"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[[ 9 25 68 88 80]\n",
            "  [49 11 95 53 99]\n",
            "  [54 67 99 15 35]\n",
            "  [25 16 61 59 17]]\n",
            "\n",
            " [[10 94 87  3 28]\n",
            "  [ 5 32  2 14 84]\n",
            "  [ 5 92 60 68  8]\n",
            "  [50 48 66 62 15]]\n",
            "\n",
            " [[56 72 81  3 95]\n",
            "  [20 99 64 54 28]\n",
            "  [57 31 49 48 40]\n",
            "  [39 45 19 65 57]]]\n",
            "[[54.  61.4 54.  35.6]\n",
            " [44.4 27.4 46.6 48.2]\n",
            " [61.4 53.  45.  45. ]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "mean = test[1].mean()indexing\n",
        "print(mean)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UcgrpoRc6Pbv",
        "outputId": "40a82f93-c315-4c4e-9158-e62e67eed331"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "41.65\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'''Add a 1D array of shape (3,) to each row of a 2D array with shape (4,3).\n",
        "Multiply a 2D array of shape (3,4) with a 1D array of shape (4,).'''\n",
        "import numpy as np\n",
        "\n",
        "# 1. Add a 1D array of shape (3,) to each row of a 2D array with shape (4, 3)\n",
        "arr_2d = np.random.randint(1, 10, (4, 3))  # A 2D array of shape (4, 3)\n",
        "arr_1d = np.array([1, 2, 3])  # A 1D array of shape (3,)\n",
        "added_result = arr_2d + arr_1d  # Broadcasting the addition\n",
        "\n",
        "# 2. Multiply a 2D array of shape (3, 4) with a 1D array of shape (4,)\n",
        "arr_2d_2 = np.random.randint(1, 10, (3, 4))  # A 2D array of shape (3, 4)\n",
        "arr_1d_2 = np.array([1, 2, 3, 4])  # A 1D array of shape (4,)\n",
        "multiplied_result = arr_2d_2 * arr_1d_2  # Element-wise multiplication (broadcasting)\n",
        "\n",
        "# Print results\n",
        "print(\"Result of adding 1D array to each row of a 2D array:\\n\", added_result)\n",
        "print(\"\\nResult of multiplying 2D array with 1D array:\\n\", multiplied_result)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "o6P68RZ-6vsf",
        "outputId": "feb2244e-0af5-4d86-e43f-15c682af9915"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result of adding 1D array to each row of a 2D array:\n",
            " [[ 4  8  5]\n",
            " [10  4  9]\n",
            " [ 6  5 12]\n",
            " [ 5  8  4]]\n",
            "\n",
            "Result of multiplying 2D array with 1D array:\n",
            " [[ 4 14 12 20]\n",
            " [ 8 14 12  4]\n",
            " [ 5 10 18 32]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n"
      ],
      "metadata": {
        "id": "ahkTEsXP7Zsy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "'''Add a 1D array of shape (4,) to each \"row\" across all \"layers\" of a 3D array with shape (3,5,4).\n",
        "Multiply a 2D array of shape (3,4) with each \"layer\" of a 3D array with shape (2,3,4).\n",
        "Scale each \"layer\" of a 3D array with shape (4,3,5) by a different scalar value from a 1D array of shape (4,).'''\n",
        "import numpy as np\n",
        "\n",
        "# Initialize arrays\n",
        "arr_3d_1 = np.random.rand(3, 5, 4)  # Shape (3,5,4)\n",
        "arr_1d = np.random.rand(4)          # Shape (4,)\n",
        "\n",
        "arr_3d_2 = np.random.rand(2, 3, 4)  # Shape (2,3,4)\n",
        "arr_2d = np.random.rand(3, 4)       # Shape (3,4)\n",
        "\n",
        "arr_3d_3 = np.random.rand(4, 3, 5)  # Shape (4,3,5)\n",
        "scalars = np.random.rand(4)         # Shape (4,)\n",
        "\n",
        "# Perform operations\n",
        "result_1 = arr_3d_1 + arr_1d  # Adding 1D array to each row across layers\n",
        "result_2 = arr_3d_2 * arr_2d  # Multiplying 2D array with each layer\n",
        "result_3 = arr_3d_3 * scalars[:, np.newaxis, np.newaxis]  # Scaling each layer by different scalars\n",
        "\n",
        "# Display results\n",
        "print(\"Result 1:\\n\", result_1)\n",
        "print(\"Result 2:\\n\", result_2)\n",
        "print(\"Result 3:\\n\", result_3)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ll3qvpobFi9V",
        "outputId": "c970eab6-8c41-47d8-d6c6-a8904246be91"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result 1:\n",
            " [[[1.36007247 0.94883407 1.03126414 1.78989272]\n",
            "  [0.93745111 1.42377951 1.44080804 1.03021148]\n",
            "  [1.08243645 0.61452077 1.2688849  1.44161255]\n",
            "  [1.41217712 0.91173872 1.16770404 1.42437385]\n",
            "  [1.13729885 0.78452534 1.17944616 1.05513972]]\n",
            "\n",
            " [[1.14684965 0.91669015 1.75719054 1.57629294]\n",
            "  [1.4656808  0.80028649 1.20185376 1.50196769]\n",
            "  [1.40662902 0.53838481 0.99114292 1.30297154]\n",
            "  [0.85532726 1.38648914 1.69572997 1.36709317]\n",
            "  [0.91386329 0.55976596 1.83718457 1.55397598]]\n",
            "\n",
            " [[1.55556659 0.81201987 1.10894825 1.1463705 ]\n",
            "  [1.55248656 0.89783123 1.52139127 1.65266109]\n",
            "  [0.94857153 0.50442068 1.59087483 1.80832996]\n",
            "  [1.64939576 0.91534629 1.49030629 1.5799275 ]\n",
            "  [1.59800053 0.58709416 1.26399555 1.26402322]]]\n",
            "Result 2:\n",
            " [[[0.06786099 0.06377474 0.40326026 0.03525881]\n",
            "  [0.01398979 0.66792714 0.02040341 0.09444526]\n",
            "  [0.0438393  0.02625208 0.06599682 0.15128444]]\n",
            "\n",
            " [[0.53556836 0.1041663  0.13142709 0.26064405]\n",
            "  [0.0154072  0.05769429 0.01599997 0.25555188]\n",
            "  [0.07019978 0.04168305 0.05439894 0.08216555]]]\n",
            "Result 3:\n",
            " [[[0.49572508 0.34622782 0.65621928 0.18937964 0.15009711]\n",
            "  [0.56223392 0.67785187 0.44152315 0.55632706 0.47789672]\n",
            "  [0.44165062 0.6795098  0.72639122 0.67099071 0.20096894]]\n",
            "\n",
            " [[0.24160264 0.11979709 0.20083944 0.11360546 0.05253969]\n",
            "  [0.19437651 0.0662494  0.23438087 0.22688625 0.14459775]\n",
            "  [0.10636473 0.16267729 0.03786207 0.22252753 0.26590461]]\n",
            "\n",
            " [[0.55969064 0.17178036 0.62246749 0.58001647 0.04570649]\n",
            "  [0.1659618  0.42324084 0.09867988 0.48694403 0.71213495]\n",
            "  [0.20509563 0.54613753 0.03339441 0.23867432 0.67794332]]\n",
            "\n",
            " [[0.26820022 0.25359247 0.39109611 0.0765517  0.0075099 ]\n",
            "  [0.08008804 0.21989377 0.20891753 0.33729171 0.36212858]\n",
            "  [0.08973029 0.18424582 0.17765103 0.02305549 0.00418562]]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'''Create a pandas Series with the values [5, 10, 15, 20, 25].\n",
        "Create a Series with values [100, 200, 300, 400, 500] and index labels ['a', 'b', 'c', 'd', 'e'].\n",
        "Create a Series from this dictionary: {'apple': 3, 'banana': 5, 'orange': 2}.\n",
        "For the Series s = pd.Series([10, 20, 30, 40, 50]):\n",
        "Find its length\n",
        "Find its mean value\n",
        "Find its maximum value'''\n",
        "import pandas as pd\n",
        "\n",
        "# 1. Create a Series with values [5, 10, 15, 20, 25]\n",
        "series1 = pd.Series([5, 10, 15, 20, 25])\n",
        "print(\"Series 1:\\n\", series1)\n",
        "\n",
        "# 2. Create a Series with values [100, 200, 300, 400, 500] and index labels ['a', 'b', 'c', 'd', 'e']\n",
        "series2 = pd.Series([100, 200, 300, 400, 500], index=['a', 'b', 'c', 'd', 'e'])\n",
        "print(\"\\nSeries 2:\\n\", series2)\n",
        "\n",
        "# 3. Create a Series from a dictionary\n",
        "fruit_dict = {'apple': 3, 'banana': 5, 'orange': 2}\n",
        "series3 = pd.Series(fruit_dict)\n",
        "print(\"\\nSeries 3:\\n\", series3)\n",
        "\n",
        "# 4. Perform operations on the given Series\n",
        "s = pd.Series([10, 20, 30, 40, 50])\n",
        "\n",
        "# Find its length\n",
        "length = len(s)\n",
        "\n",
        "# Find its mean value\n",
        "mean_value = s.mean()\n",
        "\n",
        "# Find its maximum value\n",
        "max_value = s.max()\n",
        "\n",
        "print(\"\\nSeries s:\")\n",
        "print(\"Length:\", length)\n",
        "print(\"Mean value:\", mean_value)\n",
        "print(\"Maximum value:\", max_value)"
      ],
      "metadata": {
        "id": "KXL4vqHmGktn"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "'''Create a DataFrame from this dictionary:\n",
        "data = {\n",
        "    'Name': ['John', 'Emma', 'Alex'],\n",
        "    'Age': [25, 30, 22],\n",
        "    'City': ['New York', 'London', 'Paris']\n",
        "}\n",
        "\n",
        "Create a simple DataFrame with 3 rows and 2 columns named 'A' and 'B' with any numbers you choose.\n",
        "Convert this list of lists into a DataFrame with column names 'Product', 'Price', 'Quantity':\n",
        "data = [\n",
        "    ['Apple', 1.2, 10],\n",
        "    ['Banana', 0.5, 15],\n",
        "    ['Orange', 0.8, 8]\n",
        "]'''\n",
        "import pandas as pd\n",
        "\n",
        "# 1. Create a DataFrame from a dictionary\n",
        "data = {\n",
        "    'Name': ['John', 'Emma', 'Alex'],\n",
        "    'Age': [25, 30, 22],\n",
        "    'City': ['New York', 'London', 'Paris']\n",
        "}\n",
        "df1 = pd.DataFrame(data)\n",
        "print(\"DataFrame 1:\\n\", df1)\n",
        "\n",
        "# 2. Create a simple DataFrame with 3 rows and 2 columns named 'A' and 'B'\n",
        "df2 = pd.DataFrame({\n",
        "    'A': [10, 20, 30],\n",
        "    'B': [40, 50, 60]\n",
        "})\n",
        "print(\"\\nDataFrame 2:\\n\", df2)\n",
        "\n",
        "# 3. Convert a list of lists into a DataFrame with column names 'Product', 'Price', 'Quantity'\n",
        "data_list = [\n",
        "    ['Apple', 1.2, 10],\n",
        "    ['Banana', 0.5, 15],\n",
        "    ['Orange', 0.8, 8]\n",
        "]\n",
        "df3 = pd.DataFrame(data_list, columns=['Product', 'Price', 'Quantity'])\n",
        "print(\"\\nDataFrame 3:\\n\", df3)"
      ],
      "metadata": {
        "id": "VLWyD7YoHoVC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "'''For the DataFrame created in question 5:\n",
        "Display the column names\n",
        "Display the first 2 rows\n",
        "Display information about the DataFrame (hint: use .info())\n",
        "Using this DataFrame:\n",
        "df = pd.DataFrame({\n",
        "    'A': [1, 2, 3],\n",
        "    'B': [4, 5, 6],\n",
        "    'C': [7, 8, 9]\n",
        "})\n",
        "\n",
        "Select column 'A'\n",
        "Select columns 'A' and 'C'\n",
        "Select the value at row 1, column 'B' '''\n",
        "import pandas as pd\n",
        "\n",
        "# DataFrame from question 5\n",
        "df1 = pd.DataFrame({\n",
        "    'Name': ['John', 'Emma', 'Alex'],\n",
        "    'Age': [25, 30, 22],\n",
        "    'City': ['New York', 'London', 'Paris']\n",
        "})\n",
        "\n",
        "# 1. Display the column names\n",
        "print(\"Column names:\", df1.columns.tolist())\n",
        "\n",
        "# 2. Display the first 2 rows\n",
        "print(\"\\nFirst 2 rows:\\n\", df1.head(2))\n",
        "\n",
        "# 3. Display information about the DataFrame\n",
        "print(\"\\nDataFrame Info:\")\n",
        "df1.info()\n",
        "\n",
        "# New DataFrame for selection operations\n",
        "df = pd.DataFrame({\n",
        "    'A': [1, 2, 3],\n",
        "    'B': [4, 5, 6],\n",
        "    'C': [7, 8, 9]\n",
        "})\n",
        "\n",
        "# 4. Select column 'A'\n",
        "column_a = df['A']\n",
        "print(\"\\nColumn A:\\n\", column_a)\n",
        "\n",
        "# 5. Select columns 'A' and 'C'\n",
        "columns_ac = df[['A', 'C']]\n",
        "print(\"\\nColumns A and C:\\n\", columns_ac)\n",
        "\n",
        "# 6. Select the value at row 1, column 'B'\n",
        "value_b1 = df.at[1, 'B']\n",
        "print(\"\\nValue at row 1, column 'B':\", value_b1)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2606zU5KJZ26",
        "outputId": "94c2c529-5a0e-43dc-a8d3-182d08471899"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Column names: ['Name', 'Age', 'City']\n",
            "\n",
            "First 2 rows:\n",
            "    Name  Age      City\n",
            "0  John   25  New York\n",
            "1  Emma   30    London\n",
            "\n",
            "DataFrame Info:\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 3 entries, 0 to 2\n",
            "Data columns (total 3 columns):\n",
            " #   Column  Non-Null Count  Dtype \n",
            "---  ------  --------------  ----- \n",
            " 0   Name    3 non-null      object\n",
            " 1   Age     3 non-null      int64 \n",
            " 2   City    3 non-null      object\n",
            "dtypes: int64(1), object(2)\n",
            "memory usage: 204.0+ bytes\n",
            "\n",
            "Column A:\n",
            " 0    1\n",
            "1    2\n",
            "2    3\n",
            "Name: A, dtype: int64\n",
            "\n",
            "Columns A and C:\n",
            "    A  C\n",
            "0  1  7\n",
            "1  2  8\n",
            "2  3  9\n",
            "\n",
            "Value at row 1, column 'B': 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'''Using this DataFrame:\n",
        "df = pd.DataFrame({\n",
        "    'Name': ['John', 'Emma', 'Alex', 'Sarah', 'Mike'],\n",
        "    'Age': [25, 30, 22, 28, 32],\n",
        "    'City': ['New York', 'London', 'Paris', 'Berlin', 'Tokyo'],\n",
        "    'Salary': [50000, 60000, 45000, 55000, 65000]\n",
        "})\n",
        "Select rows where Age > 25\n",
        "Select rows where City is 'London' or 'Paris'\n",
        "Select rows where Salary is between 45000 and 60000'''\n",
        "import pandas as pd\n",
        "\n",
        "# Creating the DataFrame\n",
        "df = pd.DataFrame({\n",
        "    'Name': ['John', 'Emma', 'Alex', 'Sarah', 'Mike'],\n",
        "    'Age': [25, 30, 22, 28, 32],\n",
        "    'City': ['New York', 'London', 'Paris', 'Berlin', 'Tokyo'],\n",
        "    'Salary': [50000, 60000, 45000, 55000, 65000]\n",
        "})\n",
        "\n",
        "# 1. Select rows where Age > 25\n",
        "age_filter = df[df['Age'] > 25]\n",
        "print(\"Rows where Age > 25:\\n\", age_filter)\n",
        "\n",
        "# 2. Select rows where City is 'London' or 'Paris'\n",
        "city_filter = df[df['City'].isin(['London', 'Paris'])]\n",
        "print(\"\\nRows where City is 'London' or 'Paris':\\n\", city_filter)\n",
        "\n",
        "# 3. Select rows where Salary is between 45000 and 60000\n",
        "salary_filter = df[(df['Salary'] >= 45000) & (df['Salary'] <= 60000)]\n",
        "print(\"\\nRows where Salary is between 45000 and 60000:\\n\", salary_filter)"
      ],
      "metadata": {
        "id": "ZORzpdUnK37O"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "'''Create a DataFrame with some missing values:\n",
        "df = pd.DataFrame({\n",
        "    'A': [1, 2, None, 4],\n",
        "    'B': [5, None, 7, 8],\n",
        "    'C': [9, 10, 11, None]\n",
        "})\n",
        "Count the number of missing values in each column\n",
        "Drop rows with any missing values\n",
        "Fill all missing values with 0\n",
        "\n",
        "Using the DataFrame from previous question:\n",
        "Fill missing values in column 'A' with the mean of column 'A'\n",
        "Fill missing values in column 'B' with the value 100\n",
        "Replace all missing values with the previous valid value (hint: use .ffill())'''\n",
        "import pandas as pd\n",
        "\n",
        "# Creating DataFrame with missing values\n",
        "df = pd.DataFrame({\n",
        "    'A': [1, 2, None, 4],\n",
        "    'B': [5, None, 7, 8],\n",
        "    'C': [9, 10, 11, None]\n",
        "})\n",
        "\n",
        "# 1. Count the number of missing values in each column\n",
        "missing_counts = df.isnull().sum()\n",
        "print(\"Missing values in each column:\\n\", missing_counts)\n",
        "\n",
        "# 2. Drop rows with any missing values\n",
        "df_dropped = df.dropna()\n",
        "print(\"\\nDataFrame after dropping rows with missing values:\\n\", df_dropped)\n",
        "\n",
        "# 3. Fill all missing values with 0\n",
        "df_filled_0 = df.fillna(0)\n",
        "print(\"\\nDataFrame after filling missing values with 0:\\n\", df_filled_0)\n",
        "\n",
        "# Handling missing values in specific ways\n",
        "df = pd.DataFrame({\n",
        "    'A': [1, 2, None, 4],\n",
        "    'B': [5, None, 7, 8],\n",
        "    'C': [9, 10, 11, None]\n",
        "})\n",
        "\n",
        "# 4. Fill missing values in column 'A' with the mean of column 'A'\n",
        "df['A'].fillna(df['A'].mean(), inplace=True)\n",
        "\n",
        "# 5. Fill missing values in column 'B' with the value 100\n",
        "df['B'].fillna(100, inplace=True)\n",
        "\n",
        "# 6. Replace all missing values with the previous valid value\n",
        "df.ffill(inplace=True)\n",
        "\n",
        "print(\"\\nFinal DataFrame after handling missing values:\\n\", df)"
      ],
      "metadata": {
        "id": "LkPDDeGVM8D_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "'''Create a DataFrame with student test scores:\n",
        "df = pd.DataFrame({\n",
        "    'Student': ['Alex', 'Bob', 'Charlie', 'David'],\n",
        "    'Math': [85, 90, 70, 80],\n",
        "    'Science': [90, 85, 75, 85],\n",
        "    'English': [80, 95, 80, 75]\n",
        "})\n",
        "\n",
        "Add a new column 'Average' that contains the average score for each student\n",
        "Sort the DataFrame by the Math scores in descending order\n",
        "Find the student with the highest Science score\n",
        "\n",
        "For the DataFrame in previous question:\n",
        "Find all students who scored above 85 in any subject\n",
        "Calculate the average score for each subject\n",
        "Add a new row for a student named 'Eve' with scores Math: 95, Science: 92, English: 88\n",
        "\n",
        "Using the following DataFrame:\n",
        "df = pd.DataFrame({\n",
        "    'Product': ['A', 'B', 'A', 'C', 'B', 'A'],\n",
        "    'Quantity': [10, 5, 15, 8, 12, 7],\n",
        "    'Price': [100, 200, 100, 150, 200, 100]\n",
        "})\n",
        "\n",
        "Calculate the total quantity for each product\n",
        "Calculate the total revenue (Quantity * Price) for each product'''\n",
        "import pandas as pd\n",
        "\n",
        "# Creating the student test scores DataFrame\n",
        "df = pd.DataFrame({\n",
        "    'Student': ['Alex', 'Bob', 'Charlie', 'David'],\n",
        "    'Math': [85, 90, 70, 80],\n",
        "    'Science': [90, 85, 75, 85],\n",
        "    'English': [80, 95, 80, 75]\n",
        "})\n",
        "\n",
        "# 1. Add a new column 'Average' that contains the average score for each student\n",
        "df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)\n",
        "print(\"DataFrame with Average Score:\\n\", df)\n",
        "\n",
        "# 2. Sort the DataFrame by the Math scores in descending order\n",
        "df_sorted_math = df.sort_values(by='Math', ascending=False)\n",
        "print(\"\\nDataFrame sorted by Math scores:\\n\", df_sorted_math)\n",
        "\n",
        "# 3. Find the student with the highest Science score\n",
        "top_science_student = df[df['Science'] == df['Science'].max()]['Student'].values[0]\n",
        "print(\"\\nStudent with the highest Science score:\", top_science_student)\n",
        "\n",
        "# 4. Find all students who scored above 85 in any subject\n",
        "students_above_85 = df[(df['Math'] > 85) | (df['Science'] > 85) | (df['English'] > 85)]\n",
        "print(\"\\nStudents who scored above 85 in any subject:\\n\", students_above_85)\n",
        "\n",
        "# 5. Calculate the average score for each subject\n",
        "average_per_subject = df[['Math', 'Science', 'English']].mean()\n",
        "print(\"\\nAverage score for each subject:\\n\", average_per_subject)\n",
        "\n",
        "# 6. Add a new row for a student named 'Eve' with scores Math: 95, Science: 92, English: 88\n",
        "df.loc[len(df)] = ['Eve', 95, 92, 88, (95+92+88)/3]\n",
        "print(\"\\nDataFrame after adding Eve:\\n\", df)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KdFsLotLOB-M",
        "outputId": "ea133d0a-0a98-4173-ac5e-0bebbb7fe28b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "DataFrame with Average Score:\n",
            "    Student  Math  Science  English  Average\n",
            "0     Alex    85       90       80     85.0\n",
            "1      Bob    90       85       95     90.0\n",
            "2  Charlie    70       75       80     75.0\n",
            "3    David    80       85       75     80.0\n",
            "\n",
            "DataFrame sorted by Math scores:\n",
            "    Student  Math  Science  English  Average\n",
            "1      Bob    90       85       95     90.0\n",
            "0     Alex    85       90       80     85.0\n",
            "3    David    80       85       75     80.0\n",
            "2  Charlie    70       75       80     75.0\n",
            "\n",
            "Student with the highest Science score: Alex\n",
            "\n",
            "Students who scored above 85 in any subject:\n",
            "   Student  Math  Science  English  Average\n",
            "0    Alex    85       90       80     85.0\n",
            "1     Bob    90       85       95     90.0\n",
            "\n",
            "Average score for each subject:\n",
            " Math       81.25\n",
            "Science    83.75\n",
            "English    82.50\n",
            "dtype: float64\n",
            "\n",
            "DataFrame after adding Eve:\n",
            "    Student  Math  Science  English    Average\n",
            "0     Alex    85       90       80  85.000000\n",
            "1      Bob    90       85       95  90.000000\n",
            "2  Charlie    70       75       80  75.000000\n",
            "3    David    80       85       75  80.000000\n",
            "4      Eve    95       92       88  91.666667\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "'''Mean Calculation: Given the data set [3, 7, 9, 12, 15], calculate the mean. What does this mean in the context of the data?\n",
        "Kurtosis Interpretation: What does kurtosis indicate about a data set? Describe how you would identify whether a data set has high or low kurtosis.\n",
        "Median vs. Mean: Explain the difference between the mean and median. When is it more appropriate to use the median instead of the mean?\n",
        "Mode Identification: Given the data set [2, 4, 4, 6, 8, 8, 8, 10], identify the mode. How would you interpret the mode in this context?\n",
        "Range Calculation: Calculate the range for the following data set: [3, 5, 8, 12, 14]. What does the range tell you about the spread of the data?\n",
        "Variance Calculation: Given the data set [1, 3, 5, 7], calculate the sample variance. What does variance tell you about the distribution of the data?\n",
        "Standard Deviation: How does standard deviation help in understanding data spread? Calculate the standard deviation for the data set [5, 7, 10, 12, 14].\n",
        "Skewness Analysis: Given the data set [2, 3, 4, 5, 100], describe the skewness of the data and explain what this means.'''\n",
        "=>"
      ],
      "metadata": {
        "id": "L7k8J3YNPz3j"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Mean Calculation\n",
        "import numpy as np\n",
        "\n",
        "data = [3, 7, 9, 12, 15]\n",
        "mean_value = np.mean(data)\n",
        "print(\"Mean:\", mean_value)\n",
        "\n",
        "# Kurtosis Interpretation\n",
        "from scipy.stats import kurtosis\n",
        "\n",
        "data = [3, 7, 9, 12, 15]\n",
        "kurtosis_value = kurtosis(data, fisher=False)\n",
        "print(\"Kurtosis:\", kurtosis_value)\n",
        "\n",
        "# Median vs. Mean\n",
        "data = [10, 20, 30, 40, 1000]\n",
        "mean_value = np.mean(data)\n",
        "median_value = np.median(data)\n",
        "print(\"Mean:\", mean_value, \"Median:\", median_value)\n",
        "\n",
        "# Mode Identification\n",
        "from scipy.stats import mode\n",
        "\n",
        "data = [2, 4, 4, 6, 8, 8, 8, 10]\n",
        "mode_value = mode(data).mode[0]\n",
        "print(\"Mode:\", mode_value)\n",
        "\n",
        "# Range Calculation\n",
        "data = [3, 5, 8, 12, 14]\n",
        "range_value = max(data) - min(data)\n",
        "print(\"Range:\", range_value)\n",
        "\n",
        "# Variance Calculation\n",
        "data = [1, 3, 5, 7]\n",
        "variance_value = np.var(data, ddof=1)\n",
        "print(\"Sample Variance:\", variance_value)\n",
        "\n",
        "# Standard Deviation Calculation\n",
        "data = [5, 7, 10, 12, 14]\n",
        "std_dev = np.std(data, ddof=1)\n",
        "print(\"Standard Deviation:\", std_dev)\n",
        "\n",
        "# Skewness Analysis\n",
        "from scipy.stats import skew\n",
        "\n",
        "data = [2, 3, 4, 5, 100]\n",
        "skewness_value = skew(data)\n",
        "print(\"Skewness:\", skewness_value)"
      ],
      "metadata": {
        "id": "si7E_tJDQz4Z"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "''' Create a dictionary with the following key-value pairs:\n",
        "\"name\": \"John\"\n",
        "\"age\": 30\n",
        "\"city\": \"New York\"\n",
        "Print the dictionary.'''\n",
        "# Creating the dictionary\n",
        "person = {\n",
        "    \"name\": \"John\",\n",
        "    \"age\": 30,\n",
        "    \"city\": \"New York\"\n",
        "}\n",
        "\n",
        "# Printing the dictionary\n",
        "print(person)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JZr6Mw30R2Bb",
        "outputId": "4916362e-4d78-4929-b742-bf19da4592e0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'name': 'John', 'age': 30, 'city': 'New York'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'''Question 21:\n",
        " Write a Python program to read the contents of a file named data.txt. Assume the file contains multiple lines of text. Print each line in the file.'''\n",
        "# Create a sample file\n",
        "with open(\"data.txt\", \"w\") as file:\n",
        "    file.write(\"Hello, this is line 1.\\n\")\n",
        "    file.write(\"This is line 2.\\n\")\n",
        "    file.write(\"And this is line 3.\\n\")\n",
        "\n",
        "print(\"File 'data.txt' created successfully.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fZHC2jQESK4q",
        "outputId": "cbe4b6c4-53d7-41fb-9598-64987fd98ed6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "File 'data.txt' created successfully.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "''' Write a Python program to create a file called output.txt and write the text \"Hello, World!\" into it. Ensure the file is saved in the current directory.'''\n",
        "# Open the file in write mode\n",
        "with open(\"output.txt\", \"w\") as file:\n",
        "    file.write(\"Hello, World!\")\n",
        "\n",
        "print(\"File 'output.txt' created successfully with text.\")\n",
        "import os\n",
        "print(\"File exists:\", os.path.exists(\"output.txt\"))#true=is created"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "874lCy1cS7TC",
        "outputId": "181e8d02-63f2-466f-cc03-29ad50de030d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "File 'output.txt' created successfully with text.\n",
            "File exists: True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "''' Create a dictionary with the key \"product\" and the value \"laptop\". Then, update the dictionary by adding\n",
        "a new key-value pair \"price\": 1000. Print the updated dictionary.'''\n",
        "# Create the dictionary\n",
        "item = {\"product\": \"laptop\"}\n",
        "\n",
        "# Update the dictionary with a new key-value pair\n",
        "item[\"price\"] = 1000\n",
        "\n",
        "# Print the updated dictionary\n",
        "print(item)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "I3W67_a9TSp4",
        "outputId": "7d6a1cd6-fa1b-4cf7-fc52-4eaa9371bdb5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'product': 'laptop', 'price': 1000}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "''' Use the with statement to open a file named example.txt for reading, and then print its contents.\n",
        "What is the advantage of using with for file handling?'''\n",
        "#create file example.txt\n",
        "import os\n",
        "\n",
        "filename = \"example.txt\"\n",
        "\n",
        "# Step 1: Check if the file exists, if not, create it\n",
        "if not os.path.exists(filename):\n",
        "    with open(filename, \"w\") as file:\n",
        "        file.write(\"This is an example file.\\nIt contains multiple lines of text.\\nHello, World!\")\n",
        "    print(f\"File '{filename}' was missing and has now been created.\")\n",
        "\n",
        "# Step 2: Read and print the file contents\n",
        "with open(filename, \"r\") as file:\n",
        "    contents = file.read()\n",
        "    print(\"\\n--- File Contents ---\")\n",
        "    print(contents)\n",
        "\n",
        "# Advantages of using 'with' for file handling\n",
        "print(\"\\n--- Advantages of Using 'with' for File Handling ---\")\n",
        "print(\"1. Ensures the file is automatically closed after operations.\")\n",
        "print(\"2. Prevents resource leaks, even if an error occurs.\")\n",
        "print(\"3. Makes the code cleaner and more readable.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DmhaCk8KT-de",
        "outputId": "8c4e11c8-78af-402b-d477-e29b4b1bf32c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "--- File Contents ---\n",
            "This is an example file.\n",
            "It contains multiple lines of text.\n",
            "Hello, World!\n",
            "\n",
            "--- Advantages of Using 'with' for File Handling ---\n",
            "1. Ensures the file is automatically closed after operations.\n",
            "2. Prevents resource leaks, even if an error occurs.\n",
            "3. Makes the code cleaner and more readable.\n"
          ]
        }
      ]
    }
  ]
}