no_classes_held= int(input("Enter no of classes held=>"))
class_attended= int(input("Enter no of classes held=>"))
attended_percentage=(class_attended/float(no_classes_held))*100
print("attended percentage",attended_percentage,"%")
if attended_percentage>75:
    print("you are allowed to write the exam")
else:
    print("you are not allowed to write the exam")