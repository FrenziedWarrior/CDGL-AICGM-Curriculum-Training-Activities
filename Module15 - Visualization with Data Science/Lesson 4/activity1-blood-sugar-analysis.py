import matplotlib.pyplot as plt

blood_sugar_men = [113, 85, 90, 150, 147, 88, 97, 117, 134, 81, 78, 81, 128]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

types = [blood_sugar_men, blood_sugar_women]

colors = ["g", "r"]

label = ["men", "women"]

# Diabetic Blood Sugar Ranges
# 80 - 100 = normal
# 100 - 125 = pre-diabetic
# above 125 = diabetic
bins = [80, 100, 125, 150]

plt.xlabel("Blood Sugar Range")
plt.ylabel("Total No. of Patients")

plt.hist([blood_sugar_men, blood_sugar_women], bins=bins, color=colors,
         label=label, orientation="horizontal")

plt.title("Blood Sugar Level Chart")
plt.legend()
plt.show()
