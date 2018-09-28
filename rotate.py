from keras.preprocessing.image import ImageDataGenerator,array_to_img,img_to_array,load_img
import scipy.ndimage

#img_dir='/home/isio/data/COSI/yuan_train/00000/00000.png'
#save_dir='/home/isio/data/COSI/yuan_train/shengcheng/'

def rotation(img_dir,save_dir,num,name):
    datagen=ImageDataGenerator(featurewise_center=False,
        samplewise_center=False,
        featurewise_std_normalization = False,
        samplewise_std_normalization = False,
        zca_whitening = False,
        rotation_range = 40,
        width_shift_range = 0.2,
        height_shift_range = 0.2,
        shear_range = 0.2,
        zoom_range = 0.2,
        channel_shift_range = 0.,
        fill_mode = 'nearest',
        cval = 0.0,
        horizontal_flip = True,
        vertical_flip = True,
        rescale = None,
        preprocessing_function = None)
    img=load_img(img_dir)
    x=img_to_array(img)
    x=x.reshape((1,)+x.shape)
    i=0
    for batch in datagen.flow(x,batch_size=1,
        save_to_dir=save_dir,save_prefix='0_'+name,save_format='png'):
        i+=1
        if i>num:
            break

#rotation(img_dir,save_dir)