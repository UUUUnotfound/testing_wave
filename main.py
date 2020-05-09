# coding: utf-8
'''
Created on Nov 25, 2019

@author: guimaizi
'''
from attack_plugin import xss_testing,sqlinj_testing,waf_test,cmd_inj
from config_module import filter_similarity,mongo_con,config_function
class main:
    def __init__(self):
        print('--------------------------\n\n')
        print('-------scaning...--------\n\n')
        print('--------------------------\n\n\n')
    def burp_test_run(self):
        '''
        : burp插件模式
        :return:
        '''
        try:
            config_=config_function.config_function()
            waf=waf_test.waf_test()
            if waf.run(config_.callback_target())!=0:
                cmd_in=cmd_inj.cmd_inj()
                cmd_in.run(config_.callback_target())
                sql_inj=sqlinj_testing.sqlinj_testing()
                sql_inj.run(config_.callback_target())
            xss=xss_testing.xss_testing()
            xss.run(config_.callback_target())
        except Exception as e:
            print(e)
        finally:
            filter=filter_similarity.filter_similarity()
            filter.run_filter(config_.callback_target())
            print('\n-------------\nfinished')
    def auto_porxy_run(self):
        '''
        : http请求代理数据库检测模式
        :return:
        '''
        try:
            mongo_cons=mongo_con.mongo_con()
            if mongo_cons.find_request_count()>=1:
                request_data=mongo_cons.callback_request()
                #print(request_data)
                xss=xss_testing.xss_testing()
                xss.run(request_data)
                sql_inj=sqlinj_testing.sqlinj_testing( )
                sql_inj.run(request_data)
                cmd_in=cmd_inj.cmd_inj()
                cmd_in.run(request_data)
        finally:
            mongo_cons.updete_request(request_data['_id'])
    def main(self):
        pass
if __name__ == '__main__':
    p1=main()
    p1.burp_test_run()
    #p1.auto_porxy_run()