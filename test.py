
from tensorboardX import SummaryWriter
import torchvision
writer = SummaryWriter('runs/embedding_example')

mnist = torchvision.datasets.MNIST('mnist', download=True)

writer.add_embedding(

mnist.train_data.reshape((-1, 28 * 28))[:100,:],

metadata=mnist.train_labels[:100],

label_img = mnist.train_data[:100,:,:].reshape((-1, 1, 28, 28)).float() / 255,

global_step=100

)
