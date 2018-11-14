class ProductFrameConfiguration:
    def __init__(self, introduction_title: str, introduction_word_count: int,
                 num_aspects: int, aspect_label_template: str, aspect_word_count: int,
                 cost_value_title: str, cost_value_count: int,
                 num_pros: int, pro_label_template: str, pro_word_count: int,
                 num_cons: int, con_label_template: str, con_word_count: int) -> None:
        super().__init__()
        self.con_word_count = con_word_count
        self.con_label_template = con_label_template
        self.num_cons = num_cons
        self.pro_word_count = pro_word_count
        self.pro_label_template = pro_label_template
        self.num_pros = num_pros
        self.cost_value_count = cost_value_count
        self.cost_value_title = cost_value_title
        self.aspect_word_count = aspect_word_count
        self.aspect_label_template = aspect_label_template
        self.num_aspects = num_aspects
        self.introduction_word_count = introduction_word_count
        self.introduction_title = introduction_title

    def aspect_label(self, index: int) -> str:
        if index < 1 or index > self.num_aspects:
            raise IndexError('Needs to be between 0 and {}'.format(self.num_aspects))
        else:
            return self.aspect_label_template.format(index)

    def pro_label(self, index: int) -> str:
        if index < 1 or index > self.num_pros:
            raise IndexError('Needs to be between 0 and {}'.format(self.num_pros))
        else:
            return self.pro_label_template.format(index)

    def con_label(self, index: int) -> str:
        if index < 1 or index > self.num_cons:
            raise IndexError('Needs to be between 0 and {}'.format(self.num_cons))
        else:
            return self.con_label_template.format(index)


if __name__ == '__main__':
    pfc = ProductFrameConfiguration(introduction_title='Product',
                                    introduction_word_count=60,
                                    num_aspects=2, aspect_label_template='Important Aspect {}', aspect_word_count=30,
                                    cost_value_title='Cost and Value', cost_value_count=30,
                                    num_pros=5, pro_label_template='Pro {}', pro_word_count=10,
                                    num_cons=2, con_label_template='Con {}', con_word_count=10)

    print('Testing aspect_label...')
    for i in range(0, 4):
        try:
            print(pfc.aspect_label(i))
        except IndexError as ie:
            print(ie)

    print('\nTesting pro_label')
    for i in range(0, 6):
        try:
            print(pfc.pro_label(i))
        except IndexError as ie:
            print(ie)

    print('\nTesting con_label')
    for i in range(0, 4):
        try:
            print(pfc.con_label(i))
        except IndexError as ie:
            print(ie)