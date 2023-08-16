import pandas as pd
import os.path


class Item:
    def __init__(self, name, price, quality, sales = 0):
        self.price = self.make_list(price)
        self.name = self.make_list(name)
        self.quality = self.make_list(quality)
        self.sales = self.make_list(sales)
        self.df = pd.DataFrame({'name': self.name,
                                'price': self.price,
                                'quality': self.quality,
                                'sales': self.sales})

    @staticmethod
    def make_list(argument):
        if isinstance(argument, list):
            return argument
        else:
            return [argument]


    def write(self, filename='res.csv'):
        if os.path.exists(filename):
            self.df.to_csv(filename, mode='a', index=False, header=False)
        else:
            self.df.to_csv(filename, index=False)
            
if __name__ == '__main__':
    item = Item('name', 500, 'good', 1000)
    item.write()
