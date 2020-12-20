import NewLifeUtils.Modules.ColorModule as cm
import NewLifeUtils.Modules.StringUtilModule as sm
import NewLifeUtils.Modules.LoggerModule as lm
import NewLifeUtils.Modules.ExceptModule as em
import NewLifeUtils.Modules.RandomModule as rm
import NewLifeUtils.Modules.TableBuildModule as tbm
import NewLifeUtils.Modules.CustomShellModule as csm
import NewLifeUtils.OneCode as octester

print('|'+sm.screate(f'{cm.FGC.RED}HELLO{cm.ACC.RESET}')+'|')
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