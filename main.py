import pandas as pd
import matplotlib.pyplot as plt


class DrawingPlots:

    def __init__(self):
        self.all_path = []

    def draw_plots(self, data_json):
        plt.rcParams["figure.figsize"] = [15, 5]
        i = 0
        data_analysis = pd.read_json(data_json)
        data_info = data_analysis.shape
        while i <= 5:
                # data_info[0]:
            temp = data_analysis.iloc[i]

            values1 = [temp['gt_corners'], temp['rb_corners']]
            values2 = [temp['mean'], temp['max'], temp['min']]
            values3 = [temp['floor_mean'], temp['floor_max'], temp['floor_min']]
            values4 = [temp['ceiling_mean'], temp['ceiling_max'], temp['ceiling_min']]

            index1 = ['gt_corners', 'rb_corners']
            index2 = ['mean', 'max', 'min']
            index3 = ['floor_mean', 'floor_max', 'floor_min']
            index4 = ['ceiling_mean', 'ceiling_max', 'ceiling_min']

            plt.title(temp['name'], fontsize=20)
            plt.bar(index1, values1, color='b')
            plt.bar(index2, values2, color='g')
            plt.bar(index3, values3, color='r')
            plt.bar(index4, values4, color='k')

            if '/' in temp['name']:
                new_name = temp['name'].replace('/', '&')
                path = 'plots/' + new_name + str(i)
                plt.savefig(path)
                self.all_path.append(path)
            else:
                path = 'plots/' + temp['name'] + str(i)
                plt.savefig(path)
                self.all_path.append(path)
            i += 1
        return print(self.all_path)

    def see_all_path(self):
        return self.all_path


if __name__ == '__main__':
    new_model = DrawingPlots()
    data_folder_json = 'deviation.json'
    new_model.draw_plots(data_folder_json)
