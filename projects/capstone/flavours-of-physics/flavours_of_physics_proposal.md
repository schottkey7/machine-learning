# Machine Learning Engineer Nanodegree
## Capstone Proposal
Nora Petrova  
June 4th, 2017

## Proposal

I have chosen to complete the "Flavours of Physics: Finding τ → μμμ" kaggle competition as my capstone project. The competition's description and formulation can be found at [its kaggle page](https://www.kaggle.com/c/flavours-of-physics).

### Domain Background
_(approx. 1-2 paragraphs)_

The [Standard Model](https://en.wikipedia.org/wiki/Standard_Model) (SM) of physics is our most successful theoretical framework to date. It describes the strong, weak and electromagnetic interactions and has been consistently experimentally verified since its formulation in the 70s. Despite its success, it fails to explain some important observed phenomena, such as, matter-antimatter asymmetry in the Universe or the structure of generations of elementary particles. Moreover, it does not predict the existence of dark matter or describes quantum gravity. However, SM, does not point to any new unexplored areas which we can look into in order to find answers to these questions. One such way is to find violations of symmetries that are widely believed to be conserved and are intrinsic to the structure of SM. One such symmetry around which this problem revolves is [lepton flavour](https://en.wikipedia.org/wiki/Flavour_(particle_physics)). If significant signal for decays which do not conserve lepton flavour (for charged particles) is found in the dataset, it would challenge some of the assumptions of the SM. The implications for such a a finding would be huge - it could lead to new physics and enrich our understanding on a fundamental level.

My motivation for picking this problem is two-fold: I have a deep interest in physics and would be very interested in bridging the gap between my physics and machine learning knowledge; and I believe this research is of great importance as it has the potential to challenge our current understanding.


### Problem Statement
_(approx. 1 paragraph)_

Given a list of collision events and their properties from the [LHCb](http://lhcb-public.web.cern.ch/lhcb-public/) experiment (mixed in with simulated data), predict whether a τ → 3μ (tau to three muons) decay happened in the selected collision. Because such events are believed to be rare or non-existent, the goal is to discover this particular decay (τ → 3μ) happening more frequently than expected. The goal is to improve the descriminating power between signal events (where the decay did occur) and background events (where it did not occur). The resulting classifier cannot be too dependent on discrepancies between real and simulated data or on τ mass.


### Datasets and Inputs
_(approx. 2-3 paragraphs)_

The datasets provided are a mixture of simulated and real data collected by the LHCb detectors observing collisions of accelerated particles with a specific mass range in which τ → 3μ decays cannot happen. For the simulated events, `signal` is set to 1 and for background events it is set to 0.

Four datasets are provided:

- `training.csv` is a labelled dataset to use for training the classifier. Background events are composed of real data and simulations.
- `check_agreement.csv` is a labelled dataset with the same features as the training dataset. It is to be used for checking the agreement between simulated and real data.
- `check_correlation.csv` is a labelled dataset (same features as the training dataset) for checking the correlation of the classifier with the tau mass.
- `test.csv` is a non-labelled (signal and background are mixed and indistinguishable) dataset which contains simulated signal events and real background data, simulated events and real data for the control channel.

More information about the datasets can be found in the [data tab of the competition page](https://www.kaggle.com/c/flavours-of-physics/data) and more information about the problem, physics background, the design of the competition and evaluation procudes can be found in the [research paper](https://kaggle2.blob.core.windows.net/competitions/kaggle/4488/media/lhcb_description_official.pdf) provided in the resources section.

### Solution Statement
_(approx. 1 paragraph)_

A solution should be provided in the form of a dataset with rows for every event in the dataset and with two columns: `id` and `prediction`. The prediction should be a floating point value between 0 and 1.0, serving as the probability that the event whose ID is `id` is a τ → 3μ decay. The proposed solution should first pass the [agreement test](https://www.kaggle.com/c/flavours-of-physics/details/agreement-test) and [correlation test](https://www.kaggle.com/c/flavours-of-physics/details/correlation-test). I will be using the provided [starter kit](https://www.kaggle.com/c/flavours-of-physics/details/starter-kit) to structure my solution as suggested by the guidelines.

### Benchmark Model
_(approximately 1-2 paragraphs)_

The best possible score that can be achieved for this competition is 1.0, or 100% accuracy in predicting the nature of collision events. I will be using the competition's leaderboard for benchmarking. There have been 3635 submissions from 673 teams to date, varying from 69.9% to 100% accuracy, with average of 97.2%.

### Evaluation Metrics
_(approx. 1-2 paragraphs)_

The evaluation metrics are defined in the [evaluation page](https://www.kaggle.com/c/flavours-of-physics/details/evaluation) of the competition. The proposed evaluation metric is the Weighed Area Under the [ROC](https://en.wikipedia.org/wiki/Receiver_operating_characteristic) curve. The ROC curve is partitioned based on the True Positive Rate (TPR). The predictions must pass two additional checks before they are scored with weighed AUC, namely the agreement test and the correlation test (mentioned above).

### Project Design
_(approx. 1 page)_

As this is a supervised machine learning problem, I will explore a variety of supervised machine learning techniques and develop solutions using as many suitable classifiers as I can find and benchmark them against one another to discover the ones with most predictive power. Because of the numerous features available (50 in total), I plan on employing grid search or similar techniques to narrow down the relevant features. I plan on using the information in the papers provided with the competition: [Search for lepton flavour violating decay](https://arxiv.org/pdf/1409.8548.pdf), [New approaches for boosting uniformity](http://iopscience.iop.org/article/10.1088/1748-0221/10/03/T03002/pdf;jsessionid=5AAFC09D0FDA99759BB891442CE2373F.c2.iopscience.cld.iop.org) and the [Flavours of Physics paper](https://kaggle2.blob.core.windows.net/competitions/kaggle/4488/media/lhcb_description_official.pdf#page=10), particularly the sections "Geometric variables in LHCb detector" and "Data feature explanation" in order to understand the relationships between the variables. Additionally, I will be performing my own independent research by looking up related papers and articles relating to similar LHC experiments, as well as experiments involving decays, in order to gain insights on the kind of information that is important for yielding accurate predictions. I will explore the existing solutions and the provided [kernels](https://www.kaggle.com/c/flavours-of-physics/kernels) for additional understanding of how others approached this problem.
