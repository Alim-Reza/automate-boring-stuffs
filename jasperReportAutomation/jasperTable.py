startOfTable = """<detail>
        <band height="132" splitType="Stretch">
            <componentElement >
                <reportElement x="0" y="60" width="556" height="60" uuid="5f02cb7d-2d32-405a-a4e4-cb55c18b49b3">
                    <property name="com.jaspersoft.studio.layout" value="com.jaspersoft.studio.editor.layout.VerticalRowLayout"/>
                    <property name="com.jaspersoft.studio.table.style.table_header" value="Table_TH"/>
                    <property name="com.jaspersoft.studio.table.style.column_header" value="Table_CH"/>
                    <property name="com.jaspersoft.studio.table.style.detail" value="Table_TD"/>
                </reportElement>
                <jr:table xmlns:jr="http://jasperreports.sourceforge.net/jasperreports/components" xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">
                    <datasetRun subDataset="items" uuid="b3dde82f-78b9-4992-a01e-21af76855c4b">
                        <datasetParameter name="service">
                            <datasetParameterExpression><![CDATA[$P{service}]]></datasetParameterExpression>
                        </datasetParameter>
                        <dataSourceExpression><![CDATA[new net.sf.jasperreports.engine.data.JRBeanCollectionDataSource($F{items})]]></dataSourceExpression>
                    </datasetRun>
                    <jr:column width="40" uuid="37d0a257-a576-43e0-8f78-99a7e03cb094">
                        <property name="com.jaspersoft.studio.components.table.model.column.name" value="Column1"/>
                        <jr:columnHeader style="Table_CH" height="30" rowSpan="1">
                            <staticText>
                                <reportElement x="0" y="0" width="40" height="30" uuid="eedd5aa6-e93b-46fa-a3d4-759c871c1e61"/>
                                <textElement textAlignment="Center">
                                    <font isBold="true"/>
                                </textElement>
                                <text><![CDATA[ক্রমিক]]></text>
                            </staticText>
                        </jr:columnHeader>
                        <jr:detailCell style="Table_TD" height="30">
                            <textField>
                                <reportElement x="0" y="0" width="40" height="30" uuid="099dcc30-1712-4914-bee2-c7294962ca23"/>
                                <textElement textAlignment="Center"/>
                                <textFieldExpression><![CDATA[$V{REPORT_COUNT}]]></textFieldExpression>
                            </textField>
                        </jr:detailCell>
                    </jr:column>
                    """

endOfTable = """</jr:table>
            </componentElement>
        </band>
    </detail>"""

variablePart = """<jr:column width="{}" uuid="37d0a257-a576-43e0-8f78-99a7e03cb098">
                        <property name="com.jaspersoft.studio.components.table.model.column.name" value="Column1"/>
                        <jr:columnHeader style="Table_CH" height="30" rowSpan="1">
                            <staticText>
                                <reportElement x="0" y="0" width="{}" height="30" uuid="eedd5aa6-e93b-46fa-a3d4-759c871c1e61"/>
                                <textElement textAlignment="Center">
                                    <font isBold="true"/>
                                </textElement>
                                <text><![CDATA[{}]]></text>
                            </staticText>
                        </jr:columnHeader>
                        <jr:detailCell style="Table_TD" height="30">
                            <textField>
                                <reportElement x="0" y="0" width="{}" height="30" uuid="099dcc30-1712-4914-bee2-c7294962ca22"/>
                                <textElement textAlignment="Center"/>
                                <textFieldExpression><![CDATA[$F{}]]></textFieldExpression>
                            </textField>
                        </jr:detailCell>
                    </jr:column>
                    """



jasperTable = startOfTable + endOfTable