import os
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# plt.ylim((0, 10))
plt.xlabel('iter')
plt.ylabel('cost')

methods = [
            # 'SA_neighbor1',
            # 'SA_neighbor2',

            # 'SA_T05',
            # 'SA_T010',
            # 'SA_T020',

            # 'tabu_neighbor1',
            # 'tabu_neighbor2',

            'tabu_list_len2',
            'tabu_list_len5',
            'tabu_list_len10',

           ]

colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
# Sort colors by hue, saturation, value and name.
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                for name, color in colors.items())
sorted_color_names = [name for i, (hsv, name) in enumerate(by_hsv) if i % 10 == 0] + [name for i, (hsv, name) in enumerate(by_hsv) if i % 20 == 0] + [name for i, (hsv, name) in enumerate(by_hsv) if i % 30 == 0]

for i, method in enumerate(methods):
    resfile = './results/' + method + '.txt'
    iter_set = []
    cost_set = []
    with open(resfile, 'r') as f:
        for line in f.readlines():
            [iter, cost] = line.split()
            iter_set.append(int(iter))
            cost_set.append(float(cost))


    plt.plot(iter_set, cost_set, color=sorted_color_names[i], marker="*", label=method)

plt.legend()
plt.savefig('./results/' + 'cur_all' + '.png')