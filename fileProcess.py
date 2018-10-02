'utility class, watch out to uncomment sections to work for functional requirement or company description classifier'

import os

class FileProcess:
    """a class to process the files"""

    NEWLINE = '\n'

    '+++++++ uncomment this section for functional requirement classifier +++++++'

    FR = 'FunctionalReq'
    FRN = 'FunctionalReqNOT'

    SOURCES = [
        ('data/FR/Commerce/FR', FR),
        ('data/FR/Commerce/FRN', FRN),
        ('data/FR/Mobile/FR', FR),
        ('data/FR/Mobile/FRN', FRN)
    ]

    '+++++++ uncomment this section for company description classifier +++++++'
    '''FR = 'CompanyDesc'
    FRN = 'CompanyDescNOT'

    SOURCES = [
        ('data/Industry/DESC', FR),
        ('data/Industry/DESCN', FRN)
    ]'''

    SKIP_FILES = {'cmds', 'DS_Store'}

    def read_files(self, path):
        for root, dir_names, file_names in os.walk(path):
            for path in dir_names:
                self.read_files(os.path.join(root, path))
            for file_name in file_names:
                if file_name not in self.SKIP_FILES:
                    file_path = os.path.join(root, file_name)
                    if os.path.isfile(file_path):
                        past_header, lines = False, []
                        f = open(file_path, encoding="latin-1")
                        for line in f:
                            # if past_header:
                            lines.append(line)
                        # elif line == NEWLINE:
                        #    past_header = True
                        f.close()
                        content = self.NEWLINE.join(lines)
                        yield file_path, content