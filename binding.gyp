{ 
    'variables':
    {   # Any variable we wish to create and define
    
    },
    'includes':
    [   # Any GYP include - or .gypi - files
        './includable.gypi' 
    ],
    'targets': 
    [
        {
            'target_name': 'action_before_install',
            'type': 'none',
            'actions': 
            [
                {
                    'action_name': 'unpack_xrm',
                    'inputs': [],
                    'outputs': 
                    [
                        '<(extracted_destination)'                              # Package destination
                    ],
                    'action': 
                    [
                        'python',                                               # Command
                        './unpack.py',                                          # First argument arg[0]
                        '<(remote_url)',                                        # Second argument arg[1]
                        '<(remote_branch)',                                     # Third argument arg[2]
                        '<(archive_name)',                                      # Fourth argument arg[3]
                        '<(archive_extension)',                                 # Fifth argument arg[4]
                        '<(archive_destination)',                               # Sixth argument arg[5]
                        '<(extracted_destination)'                              # Seventh argument arg[6]
                    ]
                }
            ]
        },
        {
            'target_name': 'action_install',
            'type': 'none',
            'dependencies': [ 'action_before_install' ],
            'actions': 
            [
                {
                    'action_name': 'install_xrm',
                    'inputs': [],
                    'outputs': 
                    [
                        '<(package_destination)'                                # Package destination
                    ],
                    'action': 
                    [
                        'python',                                               # Command
                        './disburse.py',                                        # First argument arg[0]
                        '<(archive_destination)nk-xrm-<(remote_branch)',        # Second argument arg[1]
                        '<(package_destination)',                               # Third argument arg[2]
                        '<(ignorable_files)'                                    # Fourth argument arg[3]
                    ]
                }
            ]
        }
    ]
}
