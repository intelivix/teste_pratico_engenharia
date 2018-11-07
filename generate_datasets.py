import json
from providers import DatasetItem


class Dataset(object):

    def __init__(self, size=100):
        super(Dataset, self).__init__()
        self.size = size
        self.dataset_ = [DatasetItem().new_item() for _ in range(self.size)]

    @property
    def dataset(self):
        return self.dataset_


if __name__ == '__main__':

    datasets_size = [1000, 2000, 5000, 10000, 20000, 30000]

    for n, size in enumerate(datasets_size):

        dataset = Dataset(size).dataset

        with open(f'teste_pratico_engenharia/dataset-{n}.json', 'w') as f:
            json.dump(dataset, f, indent=4)
