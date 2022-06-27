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

public enum LightDirection implements java.io.Serializable
{
    NORTH(0),
    SOUTH(1),
    EAST(2),
    WEST(3);

    public int value()
    {
        return _value;
    }

    public static LightDirection valueOf(int v)
    {
        switch(v)
        {
        case 0:
            return NORTH;
        case 1:
            return SOUTH;
        case 2:
            return EAST;
        case 3:
            return WEST;
        }
        return null;
    }

    private LightDirection(int v)
    {
        _value = v;
    }

    public void ice_write(com.zeroc.Ice.OutputStream ostr)
    {
        ostr.writeEnum(_value, 3);
    }

    public static void ice_write(com.zeroc.Ice.OutputStream ostr, LightDirection v)
    {
        if(v == null)
        {
            ostr.writeEnum(Home.LightDirection.NORTH.value(), 3);
        }
        else
        {
            ostr.writeEnum(v.value(), 3);
        }
    }

    public static LightDirection ice_read(com.zeroc.Ice.InputStream istr)
    {
        int v = istr.readEnum(3);
        return validate(v);
    }

    public static void ice_write(com.zeroc.Ice.OutputStream ostr, int tag, java.util.Optional<LightDirection> v)
    {
        if(v != null && v.isPresent())
        {
            ice_write(ostr, tag, v.get());
        }
    }

    public static void ice_write(com.zeroc.Ice.OutputStream ostr, int tag, LightDirection v)
    {
        if(ostr.writeOptional(tag, com.zeroc.Ice.OptionalFormat.Size))
        {
            ice_write(ostr, v);
        }
    }

    public static java.util.Optional<LightDirection> ice_read(com.zeroc.Ice.InputStream istr, int tag)
    {
        if(istr.readOptional(tag, com.zeroc.Ice.OptionalFormat.Size))
        {
            return java.util.Optional.of(ice_read(istr));
        }
        else
        {
            return java.util.Optional.empty();
        }
    }

    private static LightDirection validate(int v)
    {
        final LightDirection e = valueOf(v);
        if(e == null)
        {
            throw new com.zeroc.Ice.MarshalException("enumerator value " + v + " is out of range");
        }
        return e;
    }

    private final int _value;
}