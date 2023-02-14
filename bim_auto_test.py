import bim_auto_base as bim
import bim_auto_ug as ug
import bim_auto_word as word
import bim_auto_catia as catia
import bim_auto_altium_design as ad
import bim_auto_revit as revit
import sys
from loguru import logger


class TestType:
    """测试的软件"""
    REVIT = 'revit'
    CATIA = 'catia'
    CA = 'ca'
    WORD = 'word'
    UG = 'ug'


if __name__ == '__main__':
    args = sys.argv
    test_for = args[0]
    test_number = args[1]
    logger.info("python.exe bim_auto_test.py revit 20")
    logger.info(f'测试的软件为：{test_for}')
    logger.info(f'模型操作执行循环次数：{test_number}')

    for i in range(int(test_number)):
        if test_for == TestType.REVIT:
            revit.test_run()


