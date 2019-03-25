import torchvision.datasets as Datasets
import matplotlib.pyplot as plt
import os



if __name__ == "__main__":
    # vgg16 = models.vgg16(pretrained=True,num_class=10)
    mnist_test = Datasets.MNIST(r'E:\data', train=False, download=False)
    print('Test set: ', len(mnist_test))


    test_label = open(r'E:\data\MNIST\img\test_label.txt','w')
    for i,(img,label) in enumerate(mnist_test):
        img_path = os.path.join(r'E:\data\MNIST\img\test_img', str(i).zfill(5)+'.jpg')
        img.save(img_path)
        test_label.write(img_path+'\t'+str(label)+'\n')

    test_label.close()


