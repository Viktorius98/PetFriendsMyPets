import sys
import codecs
sys.stdout = codecs.getwriter('cp866')(sys.stdout,'replace')