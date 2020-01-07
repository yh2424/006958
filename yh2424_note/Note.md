# Note

## 2019.01.07
- Migrate your TensorFlow 1 code to TensorFlow 2 [link](https://www.tensorflow.org/guide/migrate)

    ```
    import tensorflow.compat.v1 as tf`
    tf.disable_v2_behavior()
    ```
    
- Simple GradientDecnet using Tensorflow-v2 [link](https://medium.com/analytics-vidhya/3-different-ways-to-perform-gradient-descent-in-tensorflow-2-0-and-ms-excel-ffc3791a160a)
    ```
    import tensorflow as tf
    def fu(x1, x2):
        return x1 ** 2.0 - x1 * 3  + x2 ** 2

    def fu_minimzie():
        return x1 ** 2.0 - x1 * 3  + x2 ** 2

    def reset():
        x1 = tf.Variable(10.0)
        x2 = tf.Variable(10.0)
        return x1, x2
    
    x1, x2 = reset()
    opt = tf.keras.optimizers.SGD(learning_rate=0.1)
    
    for i in range(50):
        print ('y = {:.1f}, x1 = {:.1f}, x2 = {:.1f}'.format(fu(x1, x2).numpy(), x1.numpy(), x2.numpy()))
        opt.minimize(fu_minimzie, var_list=[x1, x2])
    ```




## 2019.01.06
- 회사에서 코드 러닝 확인 됨. [참고](https://www.tensorflow.org/guide/keras/overview?hl=ko)

## 2019.12.29. 딥러닝 #01
- 서적 "모두의 딥러닝 (길벗)"을 통한 딥러닝 공부를 하며 남긴 노트
- 맥북에 딥러닝을 위한 파이참, 아나콘다 등 인스톨을 통한 환경설정  

    `conda .bash_profile`

    `conda create -n tutorial python=3.5 numpy scipy matplotlib spyder pandas seaborn scikit-learn h5py`

    `conda activate tutorial`

    `pip install tensorflow`  
    후에 몇가지 에러 발생

[##_Image|kage@duJNqY/btqALPRwWOE/eMey3DTVWejQa2KqO8Qu61/img.png|alignCenter|data-origin-width="0" data-origin-height="0"|에러가 발생함... (일단 보류하고 진행)||_##]

    `pip install keras`
    
    
