from datetime import datetime
from os.path import join
from pathlib import Path
import robot

tests = ['login' , 'createIssue','updateIssue']

project_root = Path(__file__).parent.absolute()

report_dir = f'{project_root }/Reports/RunAt{datetime.now().strftime("%H:%M:%S")}'
robot.run('.', include=tests , variable=[f'project_root:{project_root}'], outputdir=report_dir ,rerun=True)
