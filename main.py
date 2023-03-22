import pandas as pd
import matplotlib.pyplot as plt


class DrawingPlots:

    def draw_plots(self, data_json):
        plt.rcParams["figure.figsize"] = [15, 5]
        all_path = []
        count = 0
        data_analysis = pd.read_json(data_json)
        data_info = data_analysis.shape
        while count <= 30:
                # data_info[0]:
            temp = data_analysis.iloc[count]

            corners_values = [temp['gt_corners'], temp['rb_corners']]
            degree_values = [temp['mean'], temp['max'], temp['min']]
            floor_values = [temp['floor_mean'], temp['floor_max'], temp['floor_min']]
            ceiling_values = [temp['ceiling_mean'], temp['ceiling_max'], temp['ceiling_min']]

            corners_index = ['gt_corners', 'rb_corners']
            degree_index = ['mean', 'max', 'min']
            floor_index = ['floor_mean', 'floor_max', 'floor_min']
            ceiling_index = ['ceiling_mean', 'ceiling_max', 'ceiling_min']

            plt.title(temp['name'], fontsize=20)
            plt.bar(corners_index, corners_values, color='b')
            plt.bar(degree_index, degree_values, color='g')
            plt.bar(floor_index, floor_values, color='r')
            plt.bar(ceiling_index, ceiling_values, color='k')

            if '/' in temp['name']:
                new_name = temp['name'].replace('/', '&')
                path = 'plots/' + new_name + str(count)
                plt.savefig(path)
                all_path.append(str(path))
            else:
                path = 'plots/' + temp['name'] + '_' + str(count)
                plt.savefig(path)
                all_path.append(str(path))

            count += 1

        return all_path


if __name__ == '__main__':
    pass
    # new_model = DrawingPlots()
    # data_folder_json = 'deviation.json'
    # new_model.draw_plots(data_folder_json)
