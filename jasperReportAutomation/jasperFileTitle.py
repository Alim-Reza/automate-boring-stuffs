jasperFileTitle = """   <background>
        <band splitType="Stretch"/>
    </background>
    <title>
        <band height="75" splitType="Stretch">

            <textField>
                <reportElement x=\"%s\" y="0" width="400" height="30" uuid="d8f64194-3a5c-4744-94df-82e79ba550f9"/>
                <textElement textAlignment="Center">
                    <font size="18" isBold="true"/>
                </textElement>
                <textFieldExpression><![CDATA[$F{officeName}]]></textFieldExpression>
            </textField>
            <textField>
                <reportElement positionType="FixRelativeToBottom" x="80" y="30" width="400" height="18" uuid="c83c3484-5387-4be0-9450-8539702c2918"/>
                <textElement textAlignment="Center"/>
                <textFieldExpression><![CDATA[$F{officeAddress}]]></textFieldExpression>
            </textField>
            <textField>
                <reportElement x=\"%s\" y="48" width="400" height="16" uuid="c8731652-6f59-4fcf-b0cf-323a539135e9"/>
                <textElement textAlignment="Center">
                    <font size="10" isBold="true"/>
                </textElement>
                <textFieldExpression><![CDATA[$F{reportName}]]></textFieldExpression>
            </textField>
            <image scaleImage="RetainShape" hAlign="Center" vAlign="Middle" isUsingCache="true" onErrorType="Blank" evaluationTime="Auto">
                <reportElement x="0" y="0" width="80" height="64" uuid="8d0b6580-43b4-468d-9226-e3dabe15b6e7"/>
                <imageExpression><![CDATA[$F{logoUrl}]]></imageExpression>
            </image>
            <line>
                <reportElement x="0" y="70" width="555" height="1" uuid="7601a24a-5c6b-40a1-8ce4-1fa629b1e918"/>
            </line>

        </band>
    </title>
"""