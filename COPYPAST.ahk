^+a::
    Send, ^c ; Copy (Ctrl+C)
    ClipWait, 1 ; Wait for the clipboard to contain data for up to 1 second
    If ErrorLevel ; If ClipWait timed out
    {
        MsgBox, Clipboard did not contain any data.
        return
    }

    Send, !{Tab} ; Switch to the next window (Alt+Tab)
    Sleep, 200 ; Add a short delay to allow the window switch to complete (adjust as needed)

    Send, ^v ; Paste (Ctrl+V)
    Sleep, 200 ; Add a short delay to allow the paste operation to complete (adjust as needed)

    Send, {Enter} ; Press the Enter key
    ClipWait, 1 ; Wait for the clipboard to be empty for up to 1 second
    If ErrorLevel ; If ClipWait timed out
    {
        MsgBox, Clipboard did not become empty after paste.
        return
    }

    Send, !{Tab} ; Switch to the next window (Alt+Tab)
    Sleep, 200 ; Add a short delay to allow the window switch to complete (adjust as needed)

    Send, {Down} ; Press the Down arrow key
    return

^+z::
    Loop 10 ; Change the number 3 to the desired repetition count
    {
        Send, ^c ; Copy (Ctrl+C)
        ClipWait, 1 ; Wait for the clipboard to contain data for up to 1 second
        If ErrorLevel ; If ClipWait timed out
        {
            MsgBox, Clipboard did not contain any data.
            return
        }

        Send, !{Tab} ; Switch to the next window (Alt+Tab)
        Sleep, 200 ; Add a short delay to allow the window switch to complete (adjust as needed)

        Send, ^v ; Paste (Ctrl+V)
        Sleep, 200 ; Add a short delay to allow the paste operation to complete (adjust as needed)

        Send, {Enter} ; Press the Enter key
        ClipWait, 1 ; Wait for the clipboard to be empty for up to 1 second
        If ErrorLevel ; If ClipWait timed out
        {
            MsgBox, Clipboard did not become empty after paste.
            return
        }

        Send, !{Tab} ; Switch to the next window (Alt+Tab)
        Sleep, 200 ; Add a short delay to allow the window switch to complete (adjust as needed)

        Send, {Down} ; Press the Down arrow key
        Sleep, 200 ; Add a short delay between iterations (adjust as needed)
    }
    return
