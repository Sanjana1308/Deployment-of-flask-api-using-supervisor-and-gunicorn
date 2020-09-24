import traceback


# reload = True

capture_stdout = True
accesslog = '-'
access_log_format = '%(t)s [From IP: %({X-Forwarded-For}i)s] [%(U)s] Response info: { [status: %(s)s] [%(b)s bytes] [%(L)s sec] }'
loglevel = 'debug'


def on_starting(server):
    print('SERVER STARTING UP'.center(100, '-'))
    print('GIT INFO'.center(100, '-'))
    #try:
       # git_info()
    #except Exception as e:
        #traceback.print_exc()
    #print('END GIT INFO'.center(100, '-'))


def pre_request(worker, req):
    print('REQUEST STARTED'.center(100, '-'))


def post_request(worker, req, environ, resp):
    print('REQUEST FINISHED'.center(100, '-'))


#def git_info():
    #status = git.status()
    #print('git status:')
    #print(status)

    #commit = git.log('-1')
    #print('git log -n 1:')
    #print(commit)
