from djconsole.console import log
from djconsole.options import DjConsoleOptions as djops
from djconsole.projectstartup.django_app_create import DjangoStartupFlow
from djconsole.generate import app
from djconsole.generate import model
from djconsole.server import debug_server

def exe(action, action_type, args):
    
    if action == djops.dj_new:

        """
         If the args value not provided.
        """
        try:
            dj_new_flow = DjangoStartupFlow(action_type)
            dj_new_flow.execute()
        except:
            dj_new_flow = DjangoStartupFlow()
            dj_new_flow.execute()

    elif action == djops.dj_gen:
        _gen(action_type, args)

    elif action == djops.dj_server:
        debug_server.launch_server()

    else:
        log("Unknown action!", withError = True)

    

def _gen(second_arg, third_args):
    if third_args == None:
        return

    if second_arg == "app":
        try:
            app.dj_app_flow(third_args)
        except:
            log("Failed to generate app!", withError = True)
    elif second_arg == "model":
        try:
            model.dj_model_flow(third_args)
        except:
            log("Failed to generate model!", withError = True)

    else:
        log("Strategy of " + second_arg + " is not provided!", withError = True)
