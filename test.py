import NewLifeUtils.ColorModule as cm
import NewLifeUtils.StringUtilModule as sm
import NewLifeUtils.LoggerModule as lm
import NewLifeUtils.ExceptModule as em
import NewLifeUtils.RandomModule as rm
import NewLifeUtils.TableBuildModule as tbm
import NewLifeUtils.CustomShellModule as csm
import NewLifeUtils.FileModule as fm
import NewLifeUtils.OneCode as octester

print('|'+sm.screate(f'{cm.FGC.RED}HELLO{cm.ACC.RESET}')+'|', end = '')
print(fm.tree(r'D:\Документы\GitHub\NewLifeUtils\NewLifeUtils'))
lm.log('hi')
s = lm.rea('hi')
lm.log('hi')
lm.log('hi')
lm.log('hi')
lm.log('hi')
lm.log('hi')
em.except_print(Exception(s), 'wrn')
data = ['1','2','3','4','5','6']
t = tbm.createTable(2,[],data)
print(t)
print(rm.format_number())
csm.Shell().main()
octester.testNlu()
input()