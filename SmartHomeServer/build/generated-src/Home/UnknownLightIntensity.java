// **********************************************************************
//
// Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************
//
// Ice version 3.7.0
//
// <auto-generated>
//
// Generated from file `home.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

package Home;

public class UnknownLightIntensity extends com.zeroc.Ice.UserException
{
    public UnknownLightIntensity()
    {
        this.reason = "";
    }

    public UnknownLightIntensity(Throwable cause)
    {
        super(cause);
        this.reason = "";
    }

    public UnknownLightIntensity(String reason)
    {
        this.reason = reason;
    }

    public UnknownLightIntensity(String reason, Throwable cause)
    {
        super(cause);
        this.reason = reason;
    }

    public String ice_id()
    {
        return "::Home::UnknownLightIntensity";
    }

    public String reason;

    @Override
    protected void _writeImpl(com.zeroc.Ice.OutputStream ostr_)
    {
        ostr_.startSlice("::Home::UnknownLightIntensity", -1, true);
        ostr_.writeString(reason);
        ostr_.endSlice();
    }

    @Override
    protected void _readImpl(com.zeroc.Ice.InputStream istr_)
    {
        istr_.startSlice();
        reason = istr_.readString();
        istr_.endSlice();
    }

    public static final long serialVersionUID = 5437615480602642238L;
}
