import React, { useState } from "react";

import { Link } from "react-router-dom";

import { SidebarData } from "./SidebarData";
import iconImg from "../assets/img/icon-alini.png";

import { Layout, Menu, Image } from "antd";
const { Sider } = Layout;
const { SubMenu } = Menu;

const SideHeader = () => {
  const style = {
    width: "10%",
  };

  return <Image style={{ style }} src={iconImg} />;
};

const Sidebar = ({ collapsed, onCollapse, activeMenu, doLogOff }) => {
  const [selectedKey, setSelectedKey] = useState("0");

  const onClickSide = (name, key) => {
    activeMenu(name);
    setSelectedKey(key);
    if (name === "Logout") {
      doLogOff()
    }
  };

  return (
    <Sider collapsible collapsed={collapsed} onCollapse={onCollapse}>
      <SideHeader />

      <Menu theme="dark" defaultSelectedKeys={[{ selectedKey }]} mode="inline">
        {SidebarData.map((item, index) => {
          if (item.type === "menu") {
            return (
              <Menu.Item key={index} icon={item.icon}>
                <Link
                  to={item.path}
                  onClick={() => onClickSide(item.title, index)}
                />
                {item.title}
              </Menu.Item>
            );
          } else {
            return (
              <SubMenu key={index} icon={item.icon} title={item.title}>
                {item.sub.map((sub_item, sub_index) => {
                  return (
                    <Menu.Item
                      key={item.title + sub_index}
                      icon={sub_item.icon}
                    >
                      <Link
                        to={sub_item.path}
                        onClick={() =>
                          onClickSide(sub_item.title, item.title + sub_index)
                        }
                      />
                      {sub_item.title}
                    </Menu.Item>
                  );
                })}
              </SubMenu>
            );
          }
        })}
      </Menu>
    </Sider>
  );
};

export default Sidebar;
