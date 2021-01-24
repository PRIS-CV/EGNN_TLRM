Code release for the paper: ATRM: ATTENTION-BASED TASK-LEVEL RELATION MODULE FOR GNN-BASEDFEW-SHOT LEARNING.


### Platform
This code was developed and tested with pytorch version 1.0.1


### Training

```
# ************************** miniImagenet, 5way 1shot *****************************
$ python3 train.py --dataset mini --num_ways 5 --num_shots 1 --transductive False
$ python3 train.py --dataset mini --num_ways 5 --num_shots 1 --transductive True

# ************************** miniImagenet, 5way 5shot *****************************
$ python3 train.py --dataset mini --num_ways 5 --num_shots 5 --transductive False
$ python3 train.py --dataset mini --num_ways 5 --num_shots 5 --transductive True


# **************** miniImagenet, 5way 5shot, 20% labeled (semi) *********************
$ python3 train.py --dataset mini --num_ways 5 --num_shots 5 --num_unlabeled 4 --transductive False
$ python3 train.py --dataset mini --num_ways 5 --num_shots 5 --num_unlabeled 4 --transductive True

```

### Evaluation

```
$ python3 eval.py --test_model D-mini_N-5_K-1_U-0_L-3_B-40_T-True
```


### References

Our code is based on Kim's contribution. Specifically, except for our core design ATTENTION-BASED TASK-LEVEL RELATION MODULE, everything else （e.g. backbone, dataset, EGNN, evaluation standards, hyper-parameters）are built on and integrated in https://github.com/khy0809/fewshot-egnn.