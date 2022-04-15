import os
import shutil
import random
#updated to import you model
import DenseNet161_cross_val


class cross_holder:
    def __init__(self):
        """
        Update: create an empty list for each ml class
        """
        self.airport = []
        self.dam = []
        self.factory_or_powerplant = []
        self.hospital = []
        self.solar_farm = []
        self.water_treatment_facility = []

    def data_pull(self,lst,label):
      """
      :param lst: The list containing either testing or training data files
      :param label: The current label (e.g. airport, dam ect. (in the test case))
      :return: Nothing
      """
      selected_class = getattr(self, label)
      selected_class.append(lst)

    def random_random(self,label,k):
      """
      This function shuffles the testing and training lists k times. This is done to combat the pseudorandom effect in python.
      :param label: The current label (e.g. airport, dam ect.)
      :param k: How many random shuffles will be conducted
      :return: Nothing
      """
      count =0
      while count <=k:
          random.shuffle(label)
          count += 1
    def split_train_test(self,prec_train,label):
      """

      :param prec_train: By what percent is the data being split? Remaining data will be used for testing
      :param label:The current label (e.g. airport, dam ect.)
      :return:Nothing
      """
      self.training = label[:int(len(label)*prec_train)]
      self.testing = label[int(len(label) * prec_train):]



def shuffle(labels,num,testing_percent):
    """
    :param labels:Stitching function brings together the split into training and testing and random shuffle.
    :return: writes out testing and training data sets.
    """
    for n in labels:
        class_test.random_random(getattr(class_test, n), num)
        class_test.split_train_test(testing_percent, getattr(class_test, n))

        for f in class_test.testing:
            shutil.copy(f, output_dir + 'val/' + str(n))
        for f in class_test.training:
            shutil.copy(f, output_dir + 'train/' + str(n))



if __name__ == '__main__':
    ###House Keeping###
    """
    Update these file paths for your local system. Updated n for the number of folder you want to conduct
    """
    parent_dir = './tiny_data/train' #training data. Code will expect folder names that correlation with class labels
    output_dir = './scramble_output/' #output directory

    label_train='./tiny_data/train/'
    label_test='./tiny_data/val/'

    #These need to be the full file name.
    label_train_full = 'D:/x/x/x/x/x/train/' #train data file path
    label_test_full = 'D:/x/x/x/x/x/val/' #test data file path

    del_train = "D:/x/x/x/x/x/val" #val output file path
    del_test = "D:/x/x/x/x/x/train" #train output file path

    nn = 5 #number of folds (how many crosses you want in your cross validation)
    testing_percent = .8 #percent of data for training
    """
    1. Go updated cross_holder's (the class) init function
    2. Updated the model import
    3. Update your model's main() to point to the same output dir as the one you listed above
    4. Scramble does reports which run of nn you are one. Recommended that your main() reports accuracy and loss values.
    """
    ###End of Housekeeping### Did you update cross_holders init function?

    labels= []
    labels =  [n for n in os.listdir(parent_dir)] #extract labels
    class_test = cross_holder()
    for f in labels:
        """
        Iterate over each label extracted from the parent directory. Using the supplied file paths extract the name of each image to be classified. 
        With these lists iterate through each data entity sorting the entity into the correct class list. This is done for both testing and training. 
        The result of this loop is an augmented class that contains the correctly sorted name of the data entities used in both the original testing and training data sets. 
        """
        training = os.listdir(label_train+str(f))
        testing = os.listdir(label_test + str(f))
        for n in training:
            class_test.data_pull(label_train_full+str(f)+'/'+str(n),f)
        for n in testing:
            class_test.data_pull(label_test_full+str(f)+'/'+str(n),f)

    for k in range(nn):
        print("We're on run: "+str(k+1)+" of "+str(nn))
        os.mkdir(output_dir + 'train/')
        os.mkdir(output_dir + 'val/')
        [os.mkdir(output_dir + 'train/' + i) for i in labels]
        [os.mkdir(output_dir + 'val/' + i) for i in labels]
        shuffle(labels,nn,testing_percent)
        DenseNet161_cross_val.main()

        shutil.rmtree(del_train)
        shutil.rmtree(del_test)
