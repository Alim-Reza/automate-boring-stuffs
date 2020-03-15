pageFooter = """    
        <pageFooter>
        <band height="20" splitType="Stretch">
            <staticText>
                <reportElement x="127" y="0" width="300" height="14" uuid="cdf82280-c4be-4884-b07f-c683e5ca7b7f"/>
                <text><![CDATA[This is an automated generated report, no signature is required.]]></text>
            </staticText>
        </band>
    </pageFooter>
    """

lastPageFooter = """    <lastPageFooter>

        <band height="200" splitType="Stretch">
            <line>
                <reportElement x="20" y="160" width="100" height="1" uuid="7601a24a-5c6b-40a1-8ce4-1fa629b1e919"/>
            </line>
            <line>
                <reportElement x="158" y="160" width="100" height="1" uuid="7601a24a-5c6b-40a1-8ce4-1fa629b1e919"/>
            </line>
            <line>
                <reportElement x="297" y="160" width="100" height="1" uuid="7601a24a-5c6b-40a1-8ce4-1fa629b1e919"/>
            </line>
            <line>
                <reportElement x="435" y="160" width="100" height="1" uuid="7601a24a-5c6b-40a1-8ce4-1fa629b1e919"/>
            </line>


            <textField isStretchWithOverflow="true">
                <reportElement x="20" y="170" width="100" height="16"/>
                <textElement textAlignment="Center" markup="html"/>
                <textFieldExpression><![CDATA["<b>প্রস্তুতকারী</b>"]]></textFieldExpression>
            </textField>
            <textField isStretchWithOverflow="true">
                <reportElement x="158" y="170" width="100" height="16"/>
                <textElement textAlignment="Center" markup="html"/>
                <textFieldExpression><![CDATA["<b>পরীক্ষক</b>"]]></textFieldExpression>
            </textField>
            <textField isStretchWithOverflow="true">
                <reportElement x="297" y="170" width="100" height="16"/>
                <textElement textAlignment="Center" markup="html"/>
                <textFieldExpression><![CDATA["<b>সুপারিশকারী</b>"]]></textFieldExpression>
            </textField>
            <textField isStretchWithOverflow="true">
                <reportElement x="435" y="170" width="100" height="16"/>
                <textElement textAlignment="Center" markup="html"/>
                <textFieldExpression><![CDATA["<b>অনুমোদনকারী</b>"]]></textFieldExpression>
            </textField>
        </band>
    </lastPageFooter>

"""

theEnd = "</jasperReport>"

jasperEndFooter = pageFooter + theEnd
jasperEndFooterSign = lastPageFooter + theEnd