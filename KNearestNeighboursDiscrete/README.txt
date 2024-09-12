Run the K-nearest neighbours algorithm like this
python3 knn.py mushtest.csv <k> <num_of_test_points>
num_of_test_points must not exceed 3000 because the UC Irvine mushroom dataset only has 8000 data points.
file mushtest.csv can be named whatever you want, it contains the data points to test on along with their correct answers.

This algorithm runs pretty slowly. Because of the way I used selection sort.
200 test points takes about 5 minutes.
