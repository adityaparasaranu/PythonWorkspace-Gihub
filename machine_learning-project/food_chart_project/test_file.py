# from matplotlib import pyplot as plt
#
# labels = ["Carbohydrate", "Proteins", "Fats", "Vitamins and Minerals"]
# plt.pie([60, 30, 5, 5], labels=labels, wedgeprops={"edgecolor": "black"}, autopct="%1.1f%%")
# plt.title("Food Chart")
# plt.show()

# from matplotlib import pyplot as plt
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.axis('equal')
# langs = ['C', 'C++', 'Java', 'Python', 'PHP']
# students = [23,17,35,29,12]
# ax.pie(students, labels = langs)
# plt.show()
import matplotlib.pyplot as plt

plt.rcParams["pdf.use14corefonts"] = True
# trigger core fonts for PS backend
plt.rcParams["ps.useafm"] = True

chars = "AFM ftw!"
fig, ax = plt.subplots()
ax.text(0.5, 0.5, chars)

fig.savefig("AFM_PDF.pdf", format="pdf")
fig.savefig("AFM_PS.ps", format="ps")

plt.show()