from multiprocessing import Process

rdcProcess = Process
    {
        StartInfo =
            {
                FileName = Environment.ExpandEnvironmentVariables(@"%SystemRoot%\system32\cmdkey.exe"),
                Arguments = String.Format(@"/generic:TERMSRV/{0} /user:{1} /pass:{2}",
                            fp.ipAddress,
                            (String.IsNullOrEmpty(fp.accountDomain)) ? fp.accountUserName : fp.accountDomain + "\\" + fp.accountUserName,
                            fp.accountPassword),
                            WindowStyle = ProcessWindowStyle.Hidden
            }
    };
rdcProcess.Start();
rdcProcess.StartInfo.FileName = Environment.ExpandEnvironmentVariables(@"%SystemRoot%\system32\mstsc.exe");
rdcProcess.StartInfo.WindowStyle = ProcessWindowStyle.Normal;
rdcProcess.StartInfo.Arguments = String.Format("/f /v {0}", fp.ipAddress); // ip or name of computer to connect
rdcProcess.Start();