
import pyinputplus as pyip
from tools import getStudents,save_to_csv


if __name__ == "__main__":
    s_nums:int = pyip.inputInt("請輸入學生的人數(1~50):",min=1,max=50)
    students:list[dict] = getStudents(s_nums)
    fileName = pyip.inputFilename("請輸入檔案名稱(不用輸入副檔名稱):")
    format=pyip.inputChoice(["1","2"],"請問要輸出哪一個格式:\n按1.excle檔\n按2.csv\n請選擇:")
    print(format)
    if format == "1":
        print("處存為excel檔")
    else:save_to_csv(students,fileName)

